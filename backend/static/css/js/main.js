// Theme Toggle
const themeToggle = document.getElementById('themeToggle');
const html = document.documentElement;

const currentTheme = localStorage.getItem('theme') || 'light';
html.setAttribute('data-theme', currentTheme);
updateThemeIcon(currentTheme);

themeToggle.addEventListener('click', () => {
    const newTheme = html.getAttribute('data-theme') === 'light' ? 'dark' : 'light';
    html.setAttribute('data-theme', newTheme);
    localStorage.setItem('theme', newTheme);
    updateThemeIcon(newTheme);
});

function updateThemeIcon(theme) {
    themeToggle.textContent = theme === 'light' ? '🌙' : '☀️';
}

// Smooth Scroll
document.querySelectorAll('a[href^="#"]').forEach(anchor => {
    anchor.addEventListener('click', function (e) {
        e.preventDefault();
        const target = document.querySelector(this.getAttribute('href'));
        if (target) {
            target.scrollIntoView({ behavior: 'smooth' });
        }
    });
});

// Load Portfolio Data
async function loadPortfolioData() {
    try {
        const response = await fetch('/api/portfolio');
        const data = await response.json();
        
        renderSkills(data.skills);
        renderProjects(data.projects);
        renderExperience(data.experience);
    } catch (error) {
        console.error('Error loading data:', error);
    }
}

function renderSkills(skills) {
    const container = document.getElementById('skillsGrid');
    
    Object.entries(skills).forEach(([category, skillList]) => {
        const categoryDiv = document.createElement('div');
        categoryDiv.className = 'skill-category';
        categoryDiv.innerHTML = `
            <h3>${category}</h3>
            ${skillList.map(skill => `
                <div class="skill-item">
                    <div class="skill-name">
                        <span>${skill.name}</span>
                        <span>${skill.level}%</span>
                    </div>
                    <div class="skill-bar">
                        <div class="skill-fill" style="width: ${skill.level}%"></div>
                    </div>
                </div>
            `).join('')}
        `;
        container.appendChild(categoryDiv);
    });
}

function renderProjects(projects) {
    const container = document.getElementById('projectsContainer');
    
    projects.forEach(project => {
        const projectDiv = document.createElement('div');
        projectDiv.className = 'project-card';
        projectDiv.innerHTML = `
            <h3>${project.title}</h3>
            <p>${project.description}</p>
            <div class="tools">
                ${project.tools.map(tool => `<span class="tool-tag">${tool}</span>`).join('')}
            </div>
            <p class="impact"><strong>Impact:</strong> ${project.impact}</p>
            <p>${project.details}</p>
        `;
        container.appendChild(projectDiv);
    });
}

function renderExperience(experience) {
    const container = document.getElementById('experienceContainer');
    
    experience.forEach(exp => {
        const expDiv = document.createElement('div');
        expDiv.className = 'experience-item';
        expDiv.innerHTML = `
            <h3>${exp.role}</h3>
            <p class="experience-meta">${exp.company} | ${exp.duration}</p>
            <ul>
                ${exp.achievements.map(achievement => `<li>${achievement}</li>`).join('')}
            </ul>
        `;
        container.appendChild(expDiv);
    });
}

// Contact Form
document.getElementById('contactForm').addEventListener('submit', async (e) => {
    e.preventDefault();
    
    const formData = {
        name: document.getElementById('name').value,
        email: document.getElementById('email').value,
        message: document.getElementById('message').value
    };
    
    try {
        const response = await fetch('/api/contact', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify(formData)
        });
        
        if (response.ok) {
            alert('Message sent successfully!');
            document.getElementById('contactForm').reset();
        }
    } catch (error) {
        console.error('Error:', error);
        alert('Error sending message');
    }
});

// Load on page load
document.addEventListener('DOMContentLoaded', loadPortfolioData);
