// Menu functionality
const menuToggle = document.querySelector('.menu-toggle');
const menuOverlay = document.querySelector('.menu-overlay');
const menuLinks = document.querySelectorAll('.menu-link');

function toggleMenu() {
  menuToggle.classList.toggle('active');
  menuOverlay.classList.toggle('active');
  document.body.classList.toggle('no-scroll');
}

if (menuToggle) {
  menuToggle.addEventListener('click', toggleMenu);
}

menuLinks.forEach(link => {
  link.addEventListener('click', (e) => {
    const href = link.getAttribute('href');
    // If the link is an anchor on the same page, we toggle the menu immediately.
    if (href.startsWith('#')) {
      toggleMenu();
    } else if (!href.startsWith('http') || href.includes(window.location.hostname)) {
      // Internal link - trigger transition
      e.preventDefault();
      handlePageTransition(href);
    }
  });
});

// Handle Page Transitions (Simple Swipe Up)
function handlePageTransition(url) {
  let curtain = document.querySelector('.transition-curtain');
  if (!curtain) {
    curtain = document.createElement('div');
    curtain.className = 'transition-curtain';
    document.body.appendChild(curtain);
  }

  // Force reflow
  curtain.offsetHeight;
  
  // Trigger slide up
  curtain.classList.add('active');
  
  setTimeout(() => {
    window.location.href = url;
  }, 600); // Matches the new CSS transition duration
}

// Intercept Nav Links for Transition
document.querySelectorAll('.nav-links a, .logo, .footer-nav a').forEach(link => {
  link.addEventListener('click', (e) => {
    const href = link.getAttribute('href');
    if (href && !href.startsWith('#') && (!href.startsWith('http') || href.includes(window.location.hostname))) {
      e.preventDefault();
      handlePageTransition(href);
    }
  });
});

// Scroll effect for nav
const mainNav = document.querySelector('.main-nav');
window.addEventListener('scroll', () => {
  if (window.scrollY > 50) {
    mainNav.classList.add('scrolled');
  } else {
    mainNav.classList.remove('scrolled');
  }
});

// Image Slider Auto-Scroll
const imageSlider = document.querySelector('.image-slider');
if (imageSlider) {
  setInterval(() => {
    // Only auto-scroll if the user is not hovering over the slider
    if (!imageSlider.matches(':hover')) {
      const maxScrollLeft = imageSlider.scrollWidth - imageSlider.clientWidth;
      
      // If we are at the end (or very close to it), scroll back to the beginning
      if (imageSlider.scrollLeft >= maxScrollLeft - 10) {
        imageSlider.scrollTo({ left: 0, behavior: 'smooth' });
      } else {
        // Find the width of one slide + the gap
        const slideItem = imageSlider.querySelector('.slider-item');
        if (slideItem) {
          const slideWidth = slideItem.clientWidth + parseInt(window.getComputedStyle(imageSlider).gap || '24');
          imageSlider.scrollBy({ left: slideWidth, behavior: 'smooth' });
        }
      }
    }
  }, 3000); // Scroll every 3 seconds
}

// Scroll Reveal functionality
const revealElements = document.querySelectorAll('.scroll-reveal');

const revealObserver = new IntersectionObserver((entries, observer) => {
  entries.forEach(entry => {
    if (entry.isIntersecting) {
      entry.target.classList.add('visible');
    }
  });
}, {
  root: null,
  threshold: 0.15,
  rootMargin: "0px 0px -50px 0px"
});

revealElements.forEach(el => {
  revealObserver.observe(el);
});

// Arclin Sections Slider Logic (Scrollytelling)
document.addEventListener('DOMContentLoaded', () => {
  const scrollWrapper = document.getElementById('arclin-scroll-wrapper');
  if (!scrollWrapper) return;

  const titles = scrollWrapper.querySelectorAll('.arclin-slide-title');
  const fills = scrollWrapper.querySelectorAll('.arclin-progress-fill');
  const images = scrollWrapper.querySelectorAll('.arclin-side-image');
  if(titles.length === 0) return;

  let currentSlide = -1;

  function goToSlide(index) {
    if (index === currentSlide) return;
    titles.forEach((t, i) => {
      t.classList.remove('active', 'prev');
      fills[i].classList.remove('active', 'completed');
      if (images[i]) images[i].classList.remove('active');
      
      if (i < index) {
        t.classList.add('prev');
        fills[i].classList.add('completed');
      } else if (i === index) {
        t.classList.add('active');
        fills[i].classList.add('active');
        if (images[i]) images[i].classList.add('active');
      }
    });
    currentSlide = index;
  }

  window.addEventListener('scroll', () => {
    const rect = scrollWrapper.getBoundingClientRect();
    
    const scrollDistance = -rect.top;
    const scrollableHeight = rect.height - window.innerHeight;
    
    if (scrollDistance < 0) {
      goToSlide(0);
    } else if (scrollDistance > scrollableHeight) {
      goToSlide(titles.length - 1);
    } else {
      let progress = scrollDistance / scrollableHeight;
      let slideIndex = Math.floor(progress * titles.length);
      if (slideIndex >= titles.length) slideIndex = titles.length - 1;
      
      goToSlide(slideIndex);
    }
  });

  // Trigger once on load
  window.dispatchEvent(new Event('scroll'));
});

// News Filter Logic
document.addEventListener('DOMContentLoaded', () => {
  const filterBtns = document.querySelectorAll('.filter-btn');
  const newsCards = document.querySelectorAll('.news-card');

  if (filterBtns.length > 0) {
    filterBtns.forEach(btn => {
      btn.addEventListener('click', () => {
        // Remove active class from all buttons
        filterBtns.forEach(b => b.classList.remove('active'));
        // Add active class to clicked button
        btn.classList.add('active');

        const filterValue = btn.getAttribute('data-filter');

        newsCards.forEach(card => {
          if (filterValue === 'all' || card.getAttribute('data-category') === filterValue) {
            card.style.display = 'block';
          } else {
            card.style.display = 'none';
          }
        });
      });
    });
  }
});

// About Slider Logic
document.addEventListener('DOMContentLoaded', () => {
  const scrollWrapper = document.getElementById('about-scroll-wrapper');
  if (!scrollWrapper) return;
  
  const images = document.querySelectorAll('.about-slide-img');
  const progressFills = document.querySelectorAll('.about-progress-fill');
  
  let currentSlide = -1;

  function goToSlide(index) {
    if (index === currentSlide) return;
    
    images.forEach((img, i) => {
      if (i === index) img.classList.add('active');
      else img.classList.remove('active');
    });
    
    progressFills.forEach((fill, i) => {
      if (i <= index) fill.classList.add('active');
      else fill.classList.remove('active');
    });
    currentSlide = index;
  }

  window.addEventListener('scroll', () => {
    const rect = scrollWrapper.getBoundingClientRect();
    const scrollDistance = -rect.top;
    const scrollableHeight = rect.height - window.innerHeight;
    
    if (scrollDistance < 0) {
      goToSlide(0);
    } else if (scrollDistance > scrollableHeight) {
      goToSlide(images.length - 1);
    } else {
      let progress = scrollDistance / scrollableHeight;
      let slideIndex = Math.floor(progress * images.length);
      if (slideIndex >= images.length) slideIndex = images.length - 1;
      
      goToSlide(slideIndex);
    }
  });

  // Trigger once on load
  window.dispatchEvent(new Event('scroll'));
});

// Timeline scroll reveal
document.addEventListener("DOMContentLoaded", () => {
  const timelineItems = document.querySelectorAll(".timeline-item");
  
  if (timelineItems.length > 0) {
    const observer = new IntersectionObserver((entries) => {
      entries.forEach(entry => {
        if (entry.isIntersecting) {
          entry.target.classList.add("visible");
        }
      });
    }, {
      threshold: 0.1,
      rootMargin: "0px 0px -50px 0px"
    });

    timelineItems.forEach(item => {
      observer.observe(item);
    });
  }
});

// LimeIQ Sticky Timeline Scroll Logic
document.addEventListener("DOMContentLoaded", () => {
  const wrapper = document.getElementById('story-wrapper');
  const rulerFilled = document.getElementById('story-ruler-filled');
  const cards = document.querySelectorAll('.story-card');
  
  if (wrapper && cards.length > 0) {
    const numCards = cards.length;
    
    // Use requestAnimationFrame for smooth scrolling
    let ticking = false;
    
    function updateTimeline() {
      const rect = wrapper.getBoundingClientRect();
      
      // Calculate progress from 0 to 1
      // When rect.top == 0, progress = 0
      // When rect.bottom == window.innerHeight, progress = 1
      let progress = -rect.top / (rect.height - window.innerHeight);
      progress = Math.max(0, Math.min(1, progress));
      
      if (rulerFilled) {
        const p = progress * 100;
        rulerFilled.style.clipPath = `polygon(0 0, ${p}% 0, ${p}% 100%, 0 100%)`;
      }
      
      // Translate Cards
      cards.forEach((card, index) => {
        if (index === 0) return; // Base card always stays at 0
        
        const start = (index - 1) / (numCards - 1);
        const end = index / (numCards - 1);
        
        let cardProgress = (progress - start) / (end - start);
        cardProgress = Math.max(0, Math.min(1, cardProgress));
        
        const yOffset = 100 - (cardProgress * 100);
        card.style.transform = `translate3d(0, ${yOffset}vh, 0)`;
        
        if (cardProgress > 0.1) {
          card.classList.add('active');
        } else {
          card.classList.remove('active');
        }
      });
      
      // Handle the base card (index 0) active state
      if (progress < 1 / (numCards - 1)) {
        cards[0].classList.add('active');
      } else {
        cards[0].classList.remove('active');
      }
      
      ticking = false;
    }
    
    window.addEventListener('scroll', () => {
      if (!ticking) {
        window.requestAnimationFrame(updateTimeline);
        ticking = true;
      }
    });
    
    // Initial call
    updateTimeline();
  }
});

// Preloader Logic
window.addEventListener('load', () => {
  const preloader = document.getElementById('preloader');
  const signature = document.getElementById('preloader-signature');
  const preloaderContent = document.querySelector('.preloader-content');
  
  if (preloader) {
    if (preloader.classList.contains('transition-only')) {
      // Transition-only preloader for subpages: Swipe up immediately
      setTimeout(() => {
        preloader.classList.add('hidden');
        setTimeout(() => {
          preloader.style.display = 'none';
        }, 1200);
      }, 300);
    } else {
      // Full cinematic preloader for home page
      setTimeout(() => {
        if (preloaderContent) {
          preloaderContent.style.transition = 'opacity 0.4s ease';
          preloaderContent.style.opacity = '0';
          setTimeout(() => {
            preloaderContent.style.display = 'none';
          }, 400);
        }
        
        setTimeout(() => {
          if (signature) {
            signature.classList.add('show');
            signature.classList.add('draw');
          }
          
          setTimeout(() => {
            preloader.classList.add('hidden');
            setTimeout(() => {
              preloader.style.display = 'none';
            }, 1200);
          }, 1800);
        }, 600);
      }, 2400);
    }
  }
});
