// Plant Disease Detection & Solution App Frontend Logic

document.addEventListener('DOMContentLoaded', () => {
  const dropzone = document.getElementById('dropzone');
  const fileInput = document.getElementById('fileInput');
  const previewContainer = document.getElementById('previewContainer');
  const previewImage = document.getElementById('previewImage');
  const resetBtn = document.getElementById('resetBtn');
  const cameraBtn = document.getElementById('cameraBtn');
  const cameraBox = document.getElementById('cameraBox');
  const webcam = document.getElementById('webcam');
  const snapBtn = document.getElementById('snapBtn');

  const resultPlaceholder = document.getElementById('resultPlaceholder');
  const resultContent = document.getElementById('resultContent');
  const spinner = document.getElementById('spinner');

  const diseaseName = document.getElementById('diseaseName');
  const cropName = document.getElementById('cropName');
  const statusTags = document.getElementById('statusTags');
  const confidenceValue = document.getElementById('confidenceValue');
  const progressBarFill = document.getElementById('progressBarFill');

  const tabBtns = document.querySelectorAll('.tab-btn');
  const tabPanes = document.querySelectorAll('.tab-pane');

  const symptomsPane = document.getElementById('symptomsPane');
  const managementPane = document.getElementById('managementPane');
  const organicPane = document.getElementById('organicPane');
  const preventionPane = document.getElementById('preventionPane');

  const candidatesList = document.getElementById('candidatesList');
  const diseaseGrid = document.getElementById('diseaseGrid');
  const searchInput = document.getElementById('searchInput');

  let stream = null;

  // Drag and drop handlers
  ['dragenter', 'dragover', 'dragleave', 'drop'].forEach(eventName => {
    dropzone.addEventListener(eventName, preventDefaults, false);
  });

  function preventDefaults(e) {
    e.preventDefault();
    e.stopPropagation();
  }

  ['dragenter', 'dragover'].forEach(eventName => {
    dropzone.addEventListener(eventName, () => dropzone.classList.add('dragover'), false);
  });

  ['dragleave', 'drop'].forEach(eventName => {
    dropzone.addEventListener(eventName, () => dropzone.classList.remove('dragover'), false);
  });

  dropzone.addEventListener('drop', (e) => {
    const dt = e.dataTransfer;
    const files = dt.files;
    if (files.length > 0) {
      handleFile(files[0]);
    }
  });

  fileInput.addEventListener('change', (e) => {
    if (e.target.files.length > 0) {
      handleFile(e.target.files[0]);
    }
  });

  resetBtn.addEventListener('click', (e) => {
    e.stopPropagation();
    resetUpload();
  });

  function resetUpload() {
    previewContainer.style.display = 'none';
    previewImage.src = '';
    fileInput.value = '';
    resultPlaceholder.style.display = 'block';
    resultContent.style.display = 'none';
    spinner.style.display = 'none';
  }

  function handleFile(file) {
    if (!file.type.startsWith('image/')) {
      alert('Please upload a valid image file (JPG, PNG, WEBP).');
      return;
    }

    const reader = new FileReader();
    reader.onload = (e) => {
      previewImage.src = e.target.result;
      previewContainer.style.display = 'block';
      analyzeImage(file);
    };
    reader.readAsDataURL(file);
  }

  // Camera Handler
  cameraBtn.addEventListener('click', async (e) => {
    e.stopPropagation();
    if (stream) {
      stopCamera();
    } else {
      try {
        stream = await navigator.mediaDevices.getUserMedia({ video: { facingMode: 'environment' } });
        webcam.srcObject = stream;
        cameraBox.style.display = 'block';
      } catch (err) {
        alert('Could not access camera: ' + err.message);
      }
    }
  });

  function stopCamera() {
    if (stream) {
      stream.getTracks().forEach(track => track.stop());
      stream = null;
    }
    cameraBox.style.display = 'none';
  }

  snapBtn.addEventListener('click', () => {
    const canvas = document.createElement('canvas');
    canvas.width = webcam.videoWidth || 640;
    canvas.height = webcam.videoHeight || 480;
    const ctx = canvas.getContext('2d');
    ctx.drawImage(webcam, 0, 0, canvas.width, canvas.height);
    const dataUrl = canvas.toDataURL('image/jpeg');
    
    previewImage.src = dataUrl;
    previewContainer.style.display = 'block';
    stopCamera();

    // Convert data URL to Blob for analysis
    fetch(dataUrl)
      .then(res => res.blob())
      .then(blob => {
        const file = new File([blob], "camera_snap.jpg", { type: "image/jpeg" });
        analyzeImage(file);
      });
  });

  // Sample cards click handler
  document.querySelectorAll('.sample-card').forEach(card => {
    card.addEventListener('click', () => {
      const sampleType = card.dataset.sample;
      loadSampleImage(sampleType);
    });
  });

  function loadSampleImage(sampleType) {
    // Generate sample image on canvas and analyze
    const canvas = document.createElement('canvas');
    canvas.width = 300;
    canvas.height = 300;
    const ctx = canvas.getContext('2d');

    if (sampleType === 'peach_scab') {
      ctx.fillStyle = '#85583b';
      ctx.fillRect(0, 0, 300, 300);
      ctx.fillStyle = '#2d6a4f';
      ctx.beginPath();
      ctx.ellipse(150, 150, 100, 120, 0, 0, Math.PI * 2);
      ctx.fill();
      // Scab spots
      ctx.fillStyle = '#220901';
      for (let i = 0; i < 25; i++) {
        ctx.beginPath();
        ctx.arc(80 + (i*8)%140, 80 + (i*13)%140, 4 + (i%5), 0, Math.PI * 2);
        ctx.fill();
      }
    } else if (sampleType === 'apple_scab') {
      ctx.fillStyle = '#1b4332';
      ctx.fillRect(0, 0, 300, 300);
      ctx.fillStyle = '#2d6a4f';
      ctx.beginPath();
      ctx.ellipse(150, 150, 110, 90, 0.2, 0, Math.PI * 2);
      ctx.fill();
      ctx.fillStyle = '#3d2612';
      for (let i = 0; i < 30; i++) {
        ctx.beginPath();
        ctx.arc(70 + (i*9)%150, 90 + (i*11)%120, 6 + (i%4), 0, Math.PI * 2);
        ctx.fill();
      }
    } else if (sampleType === 'tomato_blight') {
      ctx.fillStyle = '#2d6a4f';
      ctx.fillRect(0, 0, 300, 300);
      ctx.fillStyle = '#e76f51';
      ctx.beginPath();
      ctx.arc(100, 120, 30, 0, Math.PI * 2);
      ctx.arc(190, 180, 40, 0, Math.PI * 2);
      ctx.fill();
      ctx.fillStyle = '#264653';
      ctx.beginPath();
      ctx.arc(100, 120, 15, 0, Math.PI * 2);
      ctx.fill();
    } else {
      // Healthy leaf
      ctx.fillStyle = '#081c15';
      ctx.fillRect(0, 0, 300, 300);
      ctx.fillStyle = '#52b788';
      ctx.beginPath();
      ctx.ellipse(150, 150, 110, 130, 0, 0, Math.PI * 2);
      ctx.fill();
      ctx.strokeStyle = '#74c69d';
      ctx.lineWidth = 3;
      ctx.beginPath();
      ctx.moveTo(150, 40);
      ctx.lineTo(150, 260);
      ctx.stroke();
    }

    const dataUrl = canvas.toDataURL('image/jpeg');
    previewImage.src = dataUrl;
    previewContainer.style.display = 'block';

    fetch(dataUrl)
      .then(res => res.blob())
      .then(blob => {
        const file = new File([blob], `${sampleType}.jpg`, { type: "image/jpeg" });
        analyzeImage(file);
      });
  }

  // Analyze Image via Server API
  async function analyzeImage(file) {
    resultPlaceholder.style.display = 'none';
    resultContent.style.display = 'none';
    spinner.style.display = 'block';

    const formData = new FormData();
    formData.append('file', file);

    try {
      const response = await fetch('/api/predict', {
        method: 'POST',
        body: formData
      });

      const data = await response.json();
      spinner.style.display = 'none';

      if (response.ok && data.status === 'success') {
        renderPrediction(data);
      } else {
        alert('Analysis error: ' + (data.error || 'Server error'));
      }
    } catch (err) {
      spinner.style.display = 'none';
      alert('Could not connect to prediction server: ' + err.message);
    }
  }

  function renderPrediction(data) {
    const pred = data.prediction;
    resultContent.style.display = 'block';

    cropName.textContent = pred.crop;
    diseaseName.textContent = pred.disease;

    // Status Tags
    statusTags.innerHTML = '';
    const isHealthy = pred.health_status.toLowerCase() === 'healthy';

    const statusTag = document.createElement('span');
    statusTag.className = `tag ${isHealthy ? 'tag-healthy' : 'tag-diseased'}`;
    statusTag.textContent = isHealthy ? 'Healthy Plant' : 'Infected / Diseased';
    statusTags.appendChild(statusTag);

    if (!isHealthy && pred.severity) {
      const sevTag = document.createElement('span');
      sevTag.className = 'tag tag-severity';
      sevTag.textContent = `Severity: ${pred.severity}`;
      statusTags.appendChild(sevTag);
    }

    // Confidence
    confidenceValue.textContent = `${pred.confidence}%`;
    setTimeout(() => {
      progressBarFill.style.width = `${pred.confidence}%`;
    }, 50);

    // Symptoms
    symptomsPane.innerHTML = '';
    if (pred.symptoms && pred.symptoms.length > 0) {
      const ul = document.createElement('ul');
      ul.className = 'solution-list';
      pred.symptoms.forEach(sym => {
        const li = document.createElement('li');
        li.textContent = sym;
        ul.appendChild(li);
      });
      symptomsPane.appendChild(ul);
    } else {
      symptomsPane.textContent = 'No specific symptoms noted.';
    }

    // Management
    managementPane.textContent = pred.management || 'No specific chemical management instructions.';

    // Organic Solution
    organicPane.textContent = pred.organic_solution || 'Maintain healthy soil and good airflow.';

    // Prevention
    preventionPane.textContent = pred.prevention || 'Practice regular field sanitation and crop rotation.';

    // Top candidates breakdown
    candidatesList.innerHTML = '<div style="font-weight:700;margin-bottom:0.5rem;font-size:0.85rem;color:#9ca3af;">ALTERNATIVE PREDICTION CANDIDATES:</div>';
    if (data.top_matches) {
      data.top_matches.forEach(item => {
        const row = document.createElement('div');
        row.className = 'candidate-item';
        row.innerHTML = `
          <span>${item.label}</span>
          <span style="font-weight:700;color:#6ee7b7;">${item.confidence}%</span>
        `;
        candidatesList.appendChild(row);
      });
    }
  }

  // Tab buttons switching
  tabBtns.forEach(btn => {
    btn.addEventListener('click', () => {
      tabBtns.forEach(b => b.classList.remove('active'));
      tabPanes.forEach(p => p.classList.remove('active'));

      btn.classList.add('active');
      const targetTab = btn.dataset.tab;
      document.getElementById(`${targetTab}Pane`).classList.add('active');
    });
  });

  // Load Disease Library Catalog
  async function loadLibrary() {
    try {
      const res = await fetch('/api/diseases');
      const data = await res.json();
      if (data.status === 'success') {
        window.diseaseDatabase = data.diseases;
        renderLibrary(data.diseases);
      }
    } catch (e) {
      console.error('Failed to load library:', e);
    }
  }

  function renderLibrary(diseases) {
    diseaseGrid.innerHTML = '';
    Object.keys(diseases).forEach(key => {
      const item = diseases[key];
      const isHealthy = item.status === 'Healthy';

      const card = document.createElement('div');
      card.className = 'disease-card';
      card.innerHTML = `
        <div class="disease-card-crop">${item.crop}</div>
        <div class="disease-card-title">${item.disease}</div>
        <span class="disease-card-status" style="background:${isHealthy ? 'rgba(16,185,129,0.2)' : 'rgba(239,68,68,0.2)'};color:${isHealthy ? '#34d399' : '#fca5a5'};">
          ${item.status}
        </span>
      `;
      card.addEventListener('click', () => {
        renderPrediction({
          status: 'success',
          prediction: {
            raw_label: key,
            crop: item.crop,
            disease: item.disease,
            health_status: item.status,
            confidence: 99.8,
            severity: item.severity,
            cause: item.cause,
            symptoms: item.symptoms,
            management: item.management,
            organic_solution: item.organic_solution,
            prevention: item.prevention
          },
          top_matches: [{"label": key, "confidence": 99.8}]
        });
        window.scrollTo({ top: 0, behavior: 'smooth' });
      });
      diseaseGrid.appendChild(card);
    });
  }

  // Search Filter
  searchInput.addEventListener('input', (e) => {
    const term = e.target.value.toLowerCase();
    if (!window.diseaseDatabase) return;
    const filtered = {};
    Object.keys(window.diseaseDatabase).forEach(key => {
      if (key.toLowerCase().includes(term) || 
          window.diseaseDatabase[key].disease.toLowerCase().includes(term) ||
          window.diseaseDatabase[key].crop.toLowerCase().includes(term)) {
        filtered[key] = window.diseaseDatabase[key];
      }
    });
    renderLibrary(filtered);
  });

  loadLibrary();
});
