const canvas = document.getElementById('drawCanvas');
const ctx = canvas.getContext('2d');
const clearBtn = document.getElementById('clearBtn');
const predictBtn = document.getElementById('predictBtn');
const predictionEl = document.getElementById('prediction');
const confidenceEl = document.getElementById('confidence');

let isDrawing = false;
let hasInk = false;
let predictTimer = null;
let isPredicting = false;

function resetCanvas() {
  ctx.fillStyle = 'white';
  ctx.fillRect(0, 0, canvas.width, canvas.height);
  ctx.strokeStyle = 'black';
  ctx.lineWidth = 15;
  ctx.lineCap = 'round';
  ctx.lineJoin = 'round';
  hasInk = false;
}

function getCanvasPoint(event) {
  const rect = canvas.getBoundingClientRect();
  const source = event.touches && event.touches.length > 0 ? event.touches[0] : event;

  return {
    x: (source.clientX - rect.left) * (canvas.width / rect.width),
    y: (source.clientY - rect.top) * (canvas.height / rect.height),
  };
}

function startDrawing(event) {
  isDrawing = true;
  const point = getCanvasPoint(event);
  ctx.beginPath();
  ctx.moveTo(point.x, point.y);
  ctx.lineTo(point.x, point.y);
  ctx.stroke();
  hasInk = true;
}

function draw(event) {
  if (!isDrawing) return;

  const point = getCanvasPoint(event);
  ctx.lineTo(point.x, point.y);
  ctx.stroke();
  hasInk = true;
}

function stopDrawing() {
  if (!isDrawing) return;

  isDrawing = false;
  ctx.closePath();
  schedulePrediction();
}

function schedulePrediction() {
  if (!hasInk) return;

  window.clearTimeout(predictTimer);
  predictTimer = window.setTimeout(() => {
    predictDigit();
  }, 250);
}

async function predictDigit() {
  if (isPredicting || !hasInk) return;

  isPredicting = true;
  predictBtn.disabled = true;
  predictionEl.textContent = '-';
  confidenceEl.className = 'confidence';
  confidenceEl.textContent = 'Đang dự đoán...';

  try {
    const response = await fetch('/predict', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ image: canvas.toDataURL('image/png') }),
    });

    const data = await response.json();
    if (!response.ok) {
      throw new Error(data.error || 'Không thể dự đoán');
    }

    predictionEl.textContent = data.prediction;
    confidenceEl.textContent = `Confidence: ${(data.confidence * 100).toFixed(2)}%`;
  } catch (error) {
    confidenceEl.className = 'confidence error';
    confidenceEl.textContent = error.message;
  } finally {
    isPredicting = false;
    predictBtn.disabled = false;
  }
}

function handleTouchStart(event) {
  event.preventDefault();
  startDrawing(event);
}

function handleTouchMove(event) {
  event.preventDefault();
  draw(event);
}

function handleTouchEnd(event) {
  event.preventDefault();
  stopDrawing();
}

canvas.addEventListener('mousedown', startDrawing);
canvas.addEventListener('mousemove', draw);
window.addEventListener('mouseup', stopDrawing);

canvas.addEventListener('touchstart', handleTouchStart, { passive: false });
canvas.addEventListener('touchmove', handleTouchMove, { passive: false });
canvas.addEventListener('touchend', handleTouchEnd, { passive: false });
canvas.addEventListener('touchcancel', handleTouchEnd, { passive: false });

clearBtn.addEventListener('click', () => {
  window.clearTimeout(predictTimer);
  resetCanvas();
  predictionEl.textContent = '-';
  confidenceEl.className = 'confidence';
  confidenceEl.textContent = 'Vẽ một chữ số rồi bấm Predict';
});

predictBtn.addEventListener('click', () => {
  window.clearTimeout(predictTimer);
  predictDigit();
});

resetCanvas();
