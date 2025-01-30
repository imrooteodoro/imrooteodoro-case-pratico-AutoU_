document.addEventListener('DOMContentLoaded', function () {
    const typewriterElement = document.getElementById('typewriter');
    const phrases = [
        "Sistema de análise de emails com IA.",
        "Classifique emails automaticamente.",
        "Detecte spam, promoções e muito mais.",
        "Processamento rápido e seguro.",
        "Tecnologia avançada para sua produtividade."
    ];
    let phraseIndex = 0;
    let charIndex = 0;
    let isDeleting = false;

    function typeWriter() {
        const currentPhrase = phrases[phraseIndex];

        if (!isDeleting && charIndex < currentPhrase.length) {
            typewriterElement.textContent = currentPhrase.substring(0, charIndex + 1);
            charIndex++;
            setTimeout(typeWriter, 100); 
        } else if (isDeleting && charIndex > 0) {
            typewriterElement.textContent = currentPhrase.substring(0, charIndex - 1);
            charIndex--;
            setTimeout(typeWriter, 50);
        } else {
            isDeleting = !isDeleting;
            if (!isDeleting) {
                phraseIndex = (phraseIndex + 1) % phrases.length; 
            }
            setTimeout(typeWriter, 1000); 
        }
    }

    typeWriter();
});