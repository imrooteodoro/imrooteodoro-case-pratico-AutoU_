function toggleTheme() {
    const html = document.documentElement;
    const isDark = html.classList.contains('dark');

    html.classList.remove(isDark ? 'dark' : 'light');
    html.classList.add(isDark ? 'light' : 'dark');

    localStorage.setItem('theme', isDark ? 'light' : 'dark');
}

function initTheme() {
    const savedTheme = localStorage.getItem('theme') || 'light';
    const systemTheme = window.matchMedia('(prefers-color-scheme: dark)').matches ? 'dark' : 'light';
    const theme = savedTheme === 'system' ? systemTheme : savedTheme;

    document.documentElement.classList.remove('light', 'dark');
    document.documentElement.classList.add(theme);
}

function showLoading() {
    const loading = document.getElementById('loading');
    loading.style.display = 'flex'; 

    const steps = ['step1', 'step2', 'step3', 'step4'];
    let currentStep = 0;

    function activateStep() {
        steps.forEach(step => {
            document.getElementById(step).classList.remove('active');
        });

        if (currentStep < steps.length) {
            document.getElementById(steps[currentStep]).classList.add('active');
            currentStep++;

            if (currentStep < steps.length) {
                setTimeout(activateStep, 1000); // Intervalo de 1 segundo entre os passos
            }
        }
    }

    activateStep();
}

function handleFileSelect(e) {
    const fileName = e.target.files[0]?.name;
    if (fileName) {
        document.getElementById('fileText').textContent = `Arquivo selecionado: ${fileName}`;
    }
}

function setupDropZone() {
    const dropZone = document.querySelector('.file-drop-zone');
    const fileInput = document.getElementById('file');

    ['dragenter', 'dragover', 'dragleave', 'drop'].forEach(eventName => {
        dropZone.addEventListener(eventName, e => {
            e.preventDefault();
            e.stopPropagation();
        });
    });

    ['dragenter', 'dragover'].forEach(eventName => {
        dropZone.addEventListener(eventName, () => {
            dropZone.classList.add('border-orange-500');
        });
    });

    ['dragleave', 'drop'].forEach(eventName => {
        dropZone.addEventListener(eventName, () => {
            dropZone.classList.remove('border-orange-500');
        });
    });

    dropZone.addEventListener('drop', function (e) {
        const dt = e.dataTransfer;
        const files = dt.files;
        fileInput.files = files;

        if (files[0]) {
            document.getElementById('fileText').textContent = `Arquivo selecionado: ${files[0].name}`;
        }
    });
}

function initPage() {
    initTheme(); 
    setupDropZone(); 

    document.getElementById('file').addEventListener('change', handleFileSelect);

    document.getElementById('uploadForm').addEventListener('submit', function () {
        showLoading(); 
    });
}

document.addEventListener('DOMContentLoaded', initPage);