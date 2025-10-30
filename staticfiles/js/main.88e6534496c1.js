// Main JavaScript file for Glitters & Giggles

document.addEventListener('DOMContentLoaded', function() {
    // Initialize all components
    initializeNewsletter();
    initializeBookingForm();
    initializeContactForm();
    initializeGallery();
    initializeAnimations();
    initializeScrollEffects();
});

// Newsletter subscription
function initializeNewsletter() {
    const newsletterForm = document.getElementById('newsletter-form');
    if (newsletterForm) {
        newsletterForm.addEventListener('submit', function(e) {
            e.preventDefault();
            const email = this.querySelector('input[type="email"]').value;

            // Show loading state
            const submitBtn = this.querySelector('button[type="submit"]');
            const originalText = submitBtn.innerHTML;
            submitBtn.innerHTML = '<span class="spinner me-2"></span>Subscribing...';
            submitBtn.disabled = true;

            // Submit via AJAX
            fetch('/api/newsletter/', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify({ email: email })
            })
            .then(response => response.json())
            .then(data => {
                showAlert('Thank you for subscribing! We\'ll keep you updated with our latest events.', 'success');
                this.reset();
            })
            .catch(error => {
                showAlert('Something went wrong. Please try again.', 'danger');
            })
            .finally(() => {
                submitBtn.innerHTML = originalText;
                submitBtn.disabled = false;
            });
        });
    }
}

// Booking form with AJAX
function initializeBookingForm() {
    const bookingForm = document.getElementById('booking-form');
    if (bookingForm) {
        bookingForm.addEventListener('submit', function(e) {
            e.preventDefault();

            const formData = new FormData(this);
            const data = Object.fromEntries(formData.entries());

            // Show loading state
            const submitBtn = this.querySelector('button[type="submit"]');
            const originalText = submitBtn.innerHTML;
            submitBtn.innerHTML = '<span class="spinner me-2"></span>Submitting...';
            submitBtn.disabled = true;

            // Submit via AJAX
            fetch('/api/bookings/', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify(data)
            })
            .then(response => response.json())
            .then(data => {
                showAlert('Thank you! Your booking request has been submitted. We\'ll contact you soon.', 'success');
                this.reset();
            })
            .catch(error => {
                showAlert('Something went wrong. Please try again.', 'danger');
            })
            .finally(() => {
                submitBtn.innerHTML = originalText;
                submitBtn.disabled = false;
            });
        });
    }
}

// Gallery filtering
function initializeGallery() {
    const filterButtons = document.querySelectorAll('.gallery-filter');
    const galleryItems = document.querySelectorAll('.gallery-item');

    filterButtons.forEach(button => {
        button.addEventListener('click', function() {
            const category = this.dataset.category;

            // Update active button
            filterButtons.forEach(btn => btn.classList.remove('active'));
            this.classList.add('active');

            // Filter gallery items
            galleryItems.forEach(item => {
                if (category === 'all' || item.dataset.category === category) {
                    item.style.display = 'block';
                } else {
                    item.style.display = 'none';
                }
            });
        });
    });
}

// Animations on scroll
function initializeAnimations() {
    const observerOptions = {
        threshold: 0.1,
        rootMargin: '0px 0px -50px 0px'
    };

    const observer = new IntersectionObserver((entries) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                entry.target.classList.add('fade-in-up');
            }
        });
    }, observerOptions);

    // Observe elements with animation classes
    document.querySelectorAll('.animate-on-scroll').forEach(el => {
        observer.observe(el);
    });
}

// Utility function to show alerts
function showAlert(message, type) {
    const alertDiv = document.createElement('div');
    alertDiv.className = `alert alert-${type} alert-dismissible fade show position-fixed`;
    alertDiv.style.cssText = 'top: 20px; right: 20px; z-index: 9999; min-width: 300px;';
    alertDiv.innerHTML = `
        ${message}
        <button type="button" class="btn-close" data-bs-dismiss="alert"></button>
    `;

    document.body.appendChild(alertDiv);

    // Auto remove after 5 seconds
    setTimeout(() => {
        if (alertDiv.parentNode) {
            alertDiv.remove();
        }
    }, 5000);
}

// Service selection for booking form
function selectService(serviceId, serviceTitle) {
    const serviceSelect = document.getElementById('id_event_type');
    const bookingModal = document.getElementById('bookingModal');

    if (serviceSelect && bookingModal) {
        serviceSelect.value = serviceId;

        // Show booking modal
        const modal = new bootstrap.Modal(bookingModal);
        modal.show();
    }
}

// Load more functionality for blog/gallery
function loadMore(endpoint, containerId, template) {
    const container = document.getElementById(containerId);
    const loadMoreBtn = document.querySelector('.load-more-btn');

    if (!container || !loadMoreBtn) return;

    loadMoreBtn.addEventListener('click', function() {
        const page = parseInt(this.dataset.page) || 1;

        fetch(`${endpoint}?page=${page + 1}`)
            .then(response => response.json())
            .then(data => {
                if (data.results && data.results.length > 0) {
                    data.results.forEach(item => {
                        const element = createElementFromTemplate(template, item);
                        container.appendChild(element);
                    });
                    this.dataset.page = page + 1;
                } else {
                    this.style.display = 'none';
                }
            })
            .catch(error => {
                console.error('Error loading more items:', error);
            });
    });
}

// Helper function to create elements from template
function createElementFromTemplate(template, data) {
    // This would be implemented based on specific template needs
    const div = document.createElement('div');
    div.innerHTML = template.replace(/\{\{(\w+)\}\}/g, (match, key) => data[key] || '');
    return div.firstElementChild;
}

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

// Form validation enhancement
function enhanceFormValidation() {
    const forms = document.querySelectorAll('form[data-validate="true"]');

    forms.forEach(form => {
        form.addEventListener('submit', function(e) {
            if (!this.checkValidity()) {
                e.preventDefault();
                e.stopPropagation();
            }
            this.classList.add('was-validated');
        });
    });
}

// Initialize form validation
enhanceFormValidation();

// Scroll effects for enhanced UX
function initializeScrollEffects() {
    const navbar = document.querySelector('.navbar');
    let lastScrollTop = 0;

    window.addEventListener('scroll', function() {
        const scrollTop = window.pageYOffset || document.documentElement.scrollTop;

        // Add shadow to navbar on scroll
        if (scrollTop > 50) {
            navbar.classList.add('navbar-scrolled');
        } else {
            navbar.classList.remove('navbar-scrolled');
        }

        lastScrollTop = scrollTop;
    });
}

// Contact form initialization
function initializeContactForm() {
    const contactForm = document.getElementById('contact-form');
    if (contactForm) {
        contactForm.addEventListener('submit', function(e) {
            e.preventDefault();

            const formData = new FormData(this);
            const data = Object.fromEntries(formData.entries());

            // Show loading state
            const submitBtn = this.querySelector('button[type="submit"]');
            const originalText = submitBtn.innerHTML;
            submitBtn.innerHTML = '<span class="spinner me-2"></span>Sending...';
            submitBtn.disabled = true;

            // Submit via AJAX to API
            fetch('/api/contact/', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify(data)
            })
            .then(response => response.json())
            .then(data => {
                showAlert('Thank you for your message! We\'ll get back to you soon.', 'success');
                this.reset();
            })
            .catch(error => {
                showAlert('Something went wrong. Please try again.', 'danger');
            })
            .finally(() => {
                submitBtn.innerHTML = originalText;
                submitBtn.disabled = false;
            });
        });
    }
}

// Enhanced gallery with lightbox
function initializeGallery() {
    const galleryItems = document.querySelectorAll('.gallery-item img');

    galleryItems.forEach(img => {
        img.addEventListener('click', function() {
            createLightbox(this.src, this.alt);
        });
    });
}

function createLightbox(src, alt) {
    const lightbox = document.createElement('div');
    lightbox.className = 'lightbox-overlay';
    lightbox.innerHTML = `
        <div class="lightbox-content">
            <img src="${src}" alt="${alt}">
            <button class="lightbox-close">&times;</button>
        </div>
    `;

    document.body.appendChild(lightbox);

    // Close lightbox
    lightbox.addEventListener('click', function(e) {
        if (e.target === this || e.target.classList.contains('lightbox-close')) {
            this.remove();
        }
    });

    // Add lightbox styles
    if (!document.querySelector('#lightbox-styles')) {
        const styles = document.createElement('style');
        styles.id = 'lightbox-styles';
        styles.textContent = `
            .lightbox-overlay {
                position: fixed;
                top: 0;
                left: 0;
                width: 100%;
                height: 100%;
                background: rgba(0,0,0,0.9);
                display: flex;
                align-items: center;
                justify-content: center;
                z-index: 9999;
            }
            .lightbox-content {
                position: relative;
                max-width: 90%;
                max-height: 90%;
            }
            .lightbox-content img {
                max-width: 100%;
                max-height: 100%;
                border-radius: 10px;
            }
            .lightbox-close {
                position: absolute;
                top: -15px;
                right: -15px;
                background: var(--primary-color);
                color: white;
                border: none;
                border-radius: 50%;
                width: 30px;
                height: 30px;
                font-size: 20px;
                cursor: pointer;
            }
        `;
        document.head.appendChild(styles);
    }
}