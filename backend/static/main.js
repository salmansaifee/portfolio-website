// ============================================
// PORTFOLIO WEBSITE - MAIN JAVASCRIPT
// ============================================

console.log('Main.js loaded successfully!');
console.log('Portfolio Data:', window.portfolioData);

// ============================================
// PROJECT MODAL FUNCTIONALITY
// ============================================

function openProjectModal(projectId) {
    console.log('Opening modal for project ID:', projectId);
    
    // Check if portfolio data exists
    if (!window.portfolioData || !window.portfolioData.projects) {
        alert('Error: Portfolio data not found!');
        console.error('Portfolio data is missing');
        return;
    }
    
    // Get project data
    const projects = window.portfolioData.projects;
    const project = projects.find(p => p.id === projectId);
    
    if (!project) {
        alert('Project not found!');
        console.error('Project with ID', projectId, 'not found');
        return;
    }
    
    console.log('Project found:', project);
    
    // Check if project has an embedded dashboard
    const dashboardSection = project.dashboard_url ? `
        <div class="modal-section">
            <h3>🎯 Interactive Dashboard</h3>
            <div class="dashboard-container">
                <iframe src="${project.dashboard_url}" 
                        frameborder="0" 
                        allowFullScreen="true"
                        class="embedded-dashboard">
                </iframe>
            </div>
            <p class="dashboard-note">
                <strong>Note:</strong> Interact with the dashboard above - use filters, hover over charts, and explore the data!
            </p>
        </div>
    ` : '';
    
    // Create modal HTML
    const modalHTML = `
        <div class="modal-overlay" id="projectModal" onclick="closeProjectModal()">
            <div class="modal-content modal-large" onclick="event.stopPropagation()">
                <span class="modal-close" onclick="closeProjectModal()">&times;</span>
                
                <h2 class="modal-title">${project.title}</h2>
                <p class="modal-description">${project.description}</p>
                
                <div class="modal-section">
                    <h3>🛠️ Tools & Technologies</h3>
                    <div class="project-tools">
                        ${project.tools.map(tool => `<span class="tool-tag">${tool}</span>`).join('')}
                    </div>
                </div>
                
                <div class="modal-section">
                    <h3>📊 Business Impact</h3>
                    <p class="project-impact-large">${project.impact}</p>
                </div>
                
                ${dashboardSection}
                
                <div class="modal-section">
                    <h3>📝 Project Details</h3>
                    <p class="project-details-text">${project.details}</p>
                </div>
                
                <div class="modal-footer">
                    <button class="btn-primary" onclick="closeProjectModal()">Close</button>
                </div>
            </div>
        </div>
    `;
    
    // Add modal to page
    document.body.insertAdjacentHTML('beforeend', modalHTML);
    
    // Prevent body scroll
    document.body.style.overflow = 'hidden';
    
    console.log('Modal opened successfully');
}

function closeProjectModal() {
    console.log('Closing modal');
    const modal = document.getElementById('projectModal');
    if (modal) {
        modal.remove();
    }
    document.body.style.overflow = 'auto';
}

// Close modal on Escape key
document.addEventListener('keydown', function(e) {
    if (e.key === 'Escape') {
        closeProjectModal();
    }
});

// ============================================
// SMOOTH SCROLLING FOR NAVIGATION
// ============================================

document.addEventListener('DOMContentLoaded', function() {
    console.log('DOM Content Loaded');
    
    // Smooth scroll for anchor links
    const navLinks = document.querySelectorAll('a[href^="#"]');
    navLinks.forEach(link => {
        link.addEventListener('click', function(e) {
            e.preventDefault();
            const targetId = this.getAttribute('href');
            if (targetId === '#') return;
            
            const targetSection = document.querySelector(targetId);
            if (targetSection) {
                targetSection.scrollIntoView({
                    behavior: 'smooth',
                    block: 'start'
                });
            }
        });
    });
});

// ============================================
// CONTACT FORM HANDLING
// ============================================

function handleContactForm(event) {
    event.preventDefault();
    
    const form = event.target;
    const formData = new FormData(form);
    
    const data = {
        name: formData.get('name'),
        email: formData.get('email'),
        message: formData.get('message')
    };
    
    console.log('Contact form submitted:', data);
    
    // Here you can add AJAX call to backend
    alert('Thank you! Your message has been sent successfully.');
    form.reset();
}

console.log('All JavaScript functions loaded successfully!');

// ============================================
// DARK MODE TOGGLE FUNCTIONALITY
// ============================================

// Check for saved theme preference or default to light mode
const currentTheme = localStorage.getItem('theme') || 'light';

// Apply saved theme on page load
if (currentTheme === 'dark') {
    document.body.classList.add('dark-mode');
}

// Theme toggle button functionality
document.addEventListener('DOMContentLoaded', function() {
    const themeToggle = document.getElementById('theme-toggle');
    
    if (themeToggle) {
        themeToggle.addEventListener('click', function() {
            document.body.classList.toggle('dark-mode');
            
            // Save theme preference
            const theme = document.body.classList.contains('dark-mode') ? 'dark' : 'light';
            localStorage.setItem('theme', theme);
            
            console.log('Theme changed to:', theme);
        });
    } else {
        console.error('Theme toggle button not found!');
    }
});


// // Main JavaScript for Portfolio Website

// console.log('✅ Main.js loaded successfully!');
// console.log('📊 Portfolio Data:', window.portfolioData);

// // ============================================
// // PROJECT MODAL FUNCTIONALITY
// // ============================================

// function openProjectModal(projectId) {
//     console.log('🔍 Opening modal for project ID:', projectId);
    
//     if (!window.portfolioData || !window.portfolioData.projects) {
//         alert('Error: Portfolio data not found!');
//         console.error('❌ Portfolio data is missing');
//         return;
//     }
    
//     const projects = window.portfolioData.projects;
//     const project = projects.find(p => p.id === projectId);
    
//     if (!project) {
//         alert('Project not found!');
//         console.error('❌ Project with ID', projectId, 'not found');
//         return;
//     }
    
//     console.log('✅ Project found:', project);
    
//     let modalHTML = `
//         <h2 class="modal-project-title">${project.title}</h2>
//         <div class="modal-project-impact">${project.impact}</div>
//         <p class="modal-project-description">${project.description}</p>
        
//         <div class="modal-project-tools">
//             ${project.tools.map(tool => `<span class="tool-tag">${tool}</span>`).join('')}
//         </div>
        
//         <div class="modal-project-details">
//             <h3>Project Details</h3>
//             <p>${project.details}</p>
//         </div>
//     `;
    
//     if (project.dashboard_url && project.dashboard_url.trim() !== '') {
//         modalHTML += `
//             <div class="dashboard-section">
//                 <h3>Live Dashboard</h3>
//                 <iframe 
//                     class="dashboard-embed" 
//                     src="${project.dashboard_url}" 
//                     frameborder="0" 
//                     allowFullScreen="true">
//                 </iframe>
//             </div>
//         `;
//     }
    
//     const modal = document.getElementById('project-modal');
//     const modalBody = document.getElementById('modal-body');
    
//     if (modal && modalBody) {
//         modalBody.innerHTML = modalHTML;
//         modal.style.display = 'block';
//         console.log('✅ Modal opened successfully');
//     } else {
//         console.error('❌ Modal elements not found');
//     }
// }

// function closeProjectModal() {
//     const modal = document.getElementById('project-modal');
//     if (modal) {
//         modal.style.display = 'none';
//         console.log('✅ Modal closed');
//     }
// }

// window.onclick = function(event) {
//     const modal = document.getElementById('project-modal');
//     if (event.target === modal) {
//         closeProjectModal();
//     }
// }

// // ============================================
// // CONTACT FORM HANDLING - FIXED VERSION
// // ============================================

// document.addEventListener('DOMContentLoaded', function() {
//     console.log('✅ DOM loaded, initializing contact form...');
    
//     const contactForm = document.getElementById('contact-form');
    
//     if (!contactForm) {
//         console.error('❌ Contact form not found!');
//         return;
//     }
    
//     contactForm.addEventListener('submit', async function(e) {
//         e.preventDefault();
//         console.log('📧 Form submitted');
        
//         const formData = {
//             name: document.getElementById('name').value,
//             email: document.getElementById('email').value,
//             message: document.getElementById('message').value
//         };
        
//         console.log('📝 Form data:', formData);
        
//         const submitButton = contactForm.querySelector('button[type="submit"]');
//         const originalButtonText = submitButton.textContent;
        
//         try {
//             submitButton.disabled = true;
//             submitButton.textContent = 'Sending...';
//             submitButton.style.opacity = '0.6';
//             submitButton.style.cursor = 'not-allowed';
            
//             console.log('📤 Sending request to /api/contact...');
            
//             const response = await fetch('/api/contact', {
//                 method: 'POST',
//                 headers: {
//                     'Content-Type': 'application/json',
//                 },
//                 body: JSON.stringify(formData)
//             });
            
//             console.log('📨 Response status:', response.status);
            
//             const result = await response.json();
//             console.log('📬 Response data:', result);
            
//             if (response.ok) {
//                 alert('✅ Message sent successfully! Thank you for reaching out.');
//                 contactForm.reset();
//                 console.log('✅ Form reset');
//             } else {
//                 alert('❌ Failed to send message: ' + (result.message || 'Unknown error'));
//                 console.error('❌ Server error:', result);
//             }
//         } catch (error) {
//             console.error('❌ Error sending message:', error);
//             alert('❌ Error sending message. Please try again or contact directly via email.');
//         } finally {
//             submitButton.disabled = false;
//             submitButton.textContent = originalButtonText;
//             submitButton.style.opacity = '1';
//             submitButton.style.cursor = 'pointer';
//         }
//     });
    
//     console.log('✅ Contact form initialized');
// });

// // ============================================
// // SMOOTH SCROLL FOR NAVIGATION
// // ============================================

// document.addEventListener('DOMContentLoaded', function() {
//     const navLinks = document.querySelectorAll('.nav-menu a[href^="#"]');
    
//     navLinks.forEach(link => {
//         link.addEventListener('click', function(e) {
//             e.preventDefault();
//             const targetId = this.getAttribute('href');
//             const targetSection = document.querySelector(targetId);
            
//             if (targetSection) {
//                 const offsetTop = targetSection.offsetTop - 120;
//                 window.scrollTo({
//                     top: offsetTop,
//                     behavior: 'smooth'
//                 });
//             }
//         });
//     });
    
//     console.log('✅ Smooth scroll initialized for', navLinks.length, 'nav links');
// });

// // ============================================
// // SKILL BAR ANIMATION ON SCROLL
// // ============================================

// function animateSkillBars() {
//     const skillBars = document.querySelectorAll('.skill-level');
    
//     skillBars.forEach(bar => {
//         const rect = bar.getBoundingClientRect();
//         const isVisible = rect.top < window.innerHeight && rect.bottom >= 0;
        
//         if (isVisible && !bar.classList.contains('animated')) {
//             const width = bar.style.width;
//             bar.style.width = '0%';
            
//             setTimeout(() => {
//                 bar.style.width = width;
//                 bar.classList.add('animated');
//             }, 100);
//         }
//     });
// }

// window.addEventListener('scroll', animateSkillBars);
// window.addEventListener('load', animateSkillBars);

// console.log('✅ All JavaScript initialized successfully!');