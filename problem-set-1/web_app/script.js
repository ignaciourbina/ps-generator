"use strict";

const CACHE_VERSION = "2024-05-01";
let questions = [];
let currentQuestionIndex = 0;
const userAnswers = {};

const quizArea = document.getElementById("quiz-area");
const questionContainer = document.getElementById("question-container");
const navigationControls = document.getElementById("navigation-controls");
const resultsContainer = document.getElementById("results-container");
resultsContainer.setAttribute("aria-live", "polite");

async function loadQuestions() {
  const res = await fetch(`question_bank.json?v=${CACHE_VERSION}`);
  if (!res.ok) {
    throw new Error("Failed to load question bank");
  }
  questions = await res.json();
}

function shuffleArray(array) {
  for (let i = array.length - 1; i > 0; i--) {
    const j = Math.floor(Math.random() * (i + 1));
    [array[i], array[j]] = [array[j], array[i]];
  }
}

function renderQuestion() {
  const q = questions[currentQuestionIndex];
  const opts = [...q.options];
  shuffleArray(opts);
  const optionsHTML = opts
    .map(
      (opt) => `
      <label class="question-option-label group hover:bg-indigo-50 hover:border-indigo-300 ${
        userAnswers[q.id] === opt.value
          ? "bg-indigo-100 border-indigo-400 ring-2 ring-indigo-300"
          : "border-gray-300"
      }">
        <input type="radio" name="q${q.id}" value="${opt.value}"
          class="form-radio h-5 w-5 text-indigo-600 focus:ring-indigo-500 mr-3 shrink-0"
          ${userAnswers[q.id] === opt.value ? "checked" : ""}
          onchange="handleOptionChange(${q.id}, '${opt.value}')">
        <span class="text-gray-700 group-hover:text-indigo-700">${opt.text}</span>
      </label>`
    )
    .join("");
  questionContainer.innerHTML = `
    <fieldset class="p-3 sm:p-5 border border-gray-200 rounded-lg shadow-sm bg-white">
      <legend class="text-base sm:text-lg text-gray-800 mb-4 leading-relaxed">
        Question ${currentQuestionIndex + 1} of ${questions.length}: ${q.text}
      </legend>
      <div class="space-y-3 options-group">${optionsHTML}</div>
    </fieldset>`;

  renderNavigation();

  if (window.MathJax && window.MathJax.typesetPromise) {
    window.MathJax.typesetPromise([questionContainer]);
  }
}

function renderNavigation() {
  navigationControls.innerHTML = "";
  if (currentQuestionIndex > 0) {
    const prevBtn = document.createElement("button");
    prevBtn.textContent = "Previous";
    prevBtn.className =
      "bg-gray-200 hover:bg-gray-300 text-gray-800 font-semibold py-2 px-4 rounded-lg shadow-md transition-colors duration-150 ease-in-out";
    prevBtn.onclick = prevQuestion;
    navigationControls.appendChild(prevBtn);
  }

  const spacer = document.createElement("div");
  spacer.className = "flex-grow";
  navigationControls.appendChild(spacer);

  if (currentQuestionIndex < questions.length - 1) {
    const nextBtn = document.createElement("button");
    nextBtn.textContent = "Next Question";
    nextBtn.className =
      "bg-indigo-600 hover:bg-indigo-700 text-white font-semibold py-2 px-4 rounded-lg shadow-md transition-colors duration-150 ease-in-out";
    nextBtn.onclick = nextQuestion;
    navigationControls.appendChild(nextBtn);
  } else {
    const submitBtn = document.createElement("button");
    submitBtn.textContent = "Submit Answers";
    submitBtn.className =
      "bg-green-600 hover:bg-green-700 text-white font-semibold py-2 px-6 rounded-lg shadow-md transition-colors duration-150 ease-in-out";
    submitBtn.onclick = submitQuiz;
    navigationControls.appendChild(submitBtn);
  }
}

function handleOptionChange(id, value) {
  userAnswers[id] = value;
  const radios = document.getElementsByName(`q${id}`);
  radios.forEach((radio) => {
    const label = radio.closest("label");
    if (radio.value === value) {
      label.classList.add("bg-indigo-100", "border-indigo-400", "ring-2", "ring-indigo-300");
      label.classList.remove("border-gray-300");
    } else {
      label.classList.remove("bg-indigo-100", "border-indigo-400", "ring-2", "ring-indigo-300");
      label.classList.add("border-gray-300");
    }
  });
}

function prevQuestion() {
  if (currentQuestionIndex > 0) {
    currentQuestionIndex--;
    renderQuestion();
  }
}

function nextQuestion() {
  if (currentQuestionIndex < questions.length - 1) {
    currentQuestionIndex++;
    renderQuestion();
  }
}

function submitQuiz() {
  quizArea.classList.add("hidden");
  resultsContainer.classList.remove("hidden");
  let correct = 0;
  let resultsHTML = `<h2 class="text-2xl sm:text-3xl font-bold text-gray-800 mb-6 text-center">Your Results</h2>`;
  questions.forEach((q, index) => {
    const userAns = userAnswers[q.id];
    const isCorrect = userAns === q.correctAnswer;
    if (isCorrect) correct++;
    const optionsFeedbackHTML = q.options
      .map((opt) => {
        let classes = "p-2 rounded-md text-sm sm:text-base ";
        let indicator = "";
        if (opt.value === q.correctAnswer) {
          classes += "bg-green-100 border border-green-300 text-green-800 font-semibold";
          indicator = userAns === opt.value ? " (Your Answer - Correct)" : " (Correct Answer)";
        } else if (userAns === opt.value) {
          classes += "bg-red-100 border border-red-300 text-red-800 font-semibold";
          indicator = " (Your Answer - Incorrect)";
        } else {
          classes += "bg-gray-50 border border-gray-200 text-gray-700";
        }
        return `<div class="${classes}">${opt.text}${indicator}</div>`;
      })
      .join("");

    resultsHTML += `
      <div class="p-4 sm:p-5 rounded-lg shadow-md mb-6 ${isCorrect ? "feedback-correct" : "feedback-incorrect"}">
        <p class="text-sm font-medium text-gray-700 mb-1">Question ${index + 1}: ${q.topic_short}</p>
        <p class="text-base sm:text-lg text-gray-900 mb-3">${q.text}</p>
        <div class="space-y-2 mb-3">${optionsFeedbackHTML}</div>
        <div class="feedback-explanation">${q.explanation}</div>
      </div>`;
  });

  resultsHTML = `
    <div class="text-center mb-8">
      <p class="text-xl sm:text-2xl font-semibold text-gray-800">You answered ${correct} out of ${questions.length} questions correctly.</p>
      <p class="text-lg text-indigo-600">${((correct / questions.length) * 100).toFixed(1)}%</p>
    </div>` + resultsHTML;

  resultsContainer.innerHTML = resultsHTML;
  if (window.MathJax && window.MathJax.typesetPromise) {
    window.MathJax.typesetPromise([resultsContainer]);
  }
}

async function startQuiz() {
  try {
    await loadQuestions();
    renderQuestion();
    document.addEventListener("keydown", (e) => {
      if (e.key === "ArrowRight") nextQuestion();
      else if (e.key === "ArrowLeft") prevQuestion();
    });
  } catch (err) {
    quizArea.innerHTML = '<p class="text-red-600">Unable to load questions.</p>';
    console.error(err);
  }
}

document.addEventListener("DOMContentLoaded", startQuiz);
