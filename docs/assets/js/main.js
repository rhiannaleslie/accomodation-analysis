// Custom JavaScript for Accommodation Analysis website

document.addEventListener('DOMContentLoaded', function() {
    // Initialize tooltips if Bootstrap tooltips are used
    var tooltipTriggerList = [].slice.call(document.querySelectorAll('[data-bs-toggle="tooltip"]'));
    var tooltipList = tooltipTriggerList.map(function (tooltipTriggerEl) {
        return new bootstrap.Tooltip(tooltipTriggerEl);
    });

    // Smooth scrolling for anchor links
    document.querySelectorAll('a[href^="#"]').forEach(anchor => {
        anchor.addEventListener('click', function (e) {
            e.preventDefault();
            const target = document.querySelector(this.getAttribute('href'));
            if (target) {
                target.scrollIntoView({
                    behavior: 'smooth',
                    block: 'start'
                });
            }
        });
    });

    // Add loading animation to map iframe
    const mapIframe = document.querySelector('.map-container iframe');
    if (mapIframe) {
        mapIframe.addEventListener('load', function() {
            this.style.opacity = '1';
        });

        // Add loading spinner
        const loadingDiv = document.createElement('div');
        loadingDiv.className = 'd-flex justify-content-center align-items-center h-100';
        loadingDiv.innerHTML = '<div class="loading"></div>';
        loadingDiv.style.position = 'absolute';
        loadingDiv.style.top = '0';
        loadingDiv.style.left = '0';
        loadingDiv.style.width = '100%';
        loadingDiv.style.height = '100%';
        loadingDiv.style.backgroundColor = 'rgba(255, 255, 255, 0.8)';
        loadingDiv.style.zIndex = '10';

        mapIframe.parentNode.insertBefore(loadingDiv, mapIframe);
        mapIframe.style.opacity = '0';
        mapIframe.style.transition = 'opacity 0.3s ease-in-out';
    }

    // Add animation to stat numbers
    const statNumbers = document.querySelectorAll('.stat-number');
    statNumbers.forEach(stat => {
        const target = parseFloat(stat.textContent);
        if (!isNaN(target)) {
            animateNumber(stat, 0, target, 1000);
        }
    });

    // Copy code blocks functionality
    document.querySelectorAll('pre').forEach(pre => {
        const button = document.createElement('button');
        button.className = 'btn btn-sm btn-outline-secondary position-absolute top-0 end-0 m-2';
        button.innerHTML = '<i class="fas fa-copy"></i>';
        button.style.zIndex = '10';

        button.addEventListener('click', function() {
            const code = pre.querySelector('code') || pre;
            navigator.clipboard.writeText(code.textContent).then(function() {
                button.innerHTML = '<i class="fas fa-check"></i>';
                setTimeout(() => {
                    button.innerHTML = '<i class="fas fa-copy"></i>';
                }, 2000);
            });
        });

        pre.style.position = 'relative';
        pre.appendChild(button);
    });
});

// Animate number counting up
function animateNumber(element, start, end, duration) {
    const startTime = performance.now();

    function update(currentTime) {
        const elapsed = currentTime - startTime;
        const progress = Math.min(elapsed / duration, 1);

        // Easing function
        const easeOutQuart = 1 - Math.pow(1 - progress, 4);
        const current = Math.floor(start + (end - start) * easeOutQuart);

        element.textContent = current;

        if (progress < 1) {
            requestAnimationFrame(update);
        }
    }

    requestAnimationFrame(update);
}

// Lazy load images
if ('IntersectionObserver' in window) {
    const imageObserver = new IntersectionObserver((entries, observer) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                const img = entry.target;
                img.src = img.dataset.src;
                img.classList.remove('lazy');
                imageObserver.unobserve(img);
            }
        });
    });

    document.querySelectorAll('img[data-src]').forEach(img => {
        imageObserver.observe(img);
    });
}

// Add print styles
const printStyles = `
@media print {
    .navbar, .btn, .card-footer, .fab {
        display: none !important;
    }

    .container {
        max-width: none !important;
        margin: 0 !important;
        padding: 0 !important;
    }

    body {
        font-size: 12pt !important;
        line-height: 1.4 !important;
    }

    h1, h2, h3, h4, h5, h6 {
        page-break-after: avoid;
    }

    .card {
        border: 1px solid #000 !important;
        break-inside: avoid;
    }
}
`;

// Add print styles to head
const style = document.createElement('style');
style.textContent = printStyles;
document.head.appendChild(style);