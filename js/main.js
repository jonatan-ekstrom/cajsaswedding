/* =============================================
   Cajsa & Filip — Wedding Website Scripts
   ============================================= */

(function () {
  'use strict';

  /* --- Countdown Timer --- */
  function initCountdown() {
    const weddingDate = new Date(2026, 4, 23, 16, 0, 0);

    function update() {
      const now = new Date();
      /* Use wall-clock diff so DST shift doesn't confuse the countdown */
      const dstOffset = (now.getTimezoneOffset() - weddingDate.getTimezoneOffset()) * 60000;
      const diff = weddingDate - now + dstOffset;

      if (diff <= 0) {
        const el = document.querySelector('.countdown');
        if (el) el.innerHTML = '<p class="countdown-message">Idag är dagen!</p>';
        return;
      }

      const days = Math.floor(diff / (1000 * 60 * 60 * 24));
      const hours = Math.floor((diff % (1000 * 60 * 60 * 24)) / (1000 * 60 * 60));
      const minutes = Math.floor((diff % (1000 * 60 * 60)) / (1000 * 60));
      const seconds = Math.floor((diff % (1000 * 60)) / 1000);

      set('countdown-days', days);
      set('countdown-hours', hours);
      set('countdown-minutes', minutes);
      set('countdown-seconds', seconds);
    }

    function set(id, value) {
      const el = document.getElementById(id);
      if (el) el.textContent = String(value).padStart(2, '0');
    }

    update();
    setInterval(update, 1000);
  }

  /* --- Nav Scroll Detection --- */
  function initNavScroll() {
    const header = document.getElementById('site-header');
    if (!header) return;
    window.addEventListener('scroll', function () {
      header.classList.toggle('scrolled', window.scrollY > 50);
    }, { passive: true });
  }

  /* --- Mobile Nav (leaf toggle) --- */
  function initMobileNav() {
    const toggle = document.querySelector('.nav-toggle');
    const menu = document.getElementById('nav-menu');
    if (!toggle || !menu) return;

    var leaf = toggle.querySelector('.nav-leaf');
    if (leaf) {
      leaf.addEventListener('animationend', function () {
        leaf.style.animation = 'none';
      });
    }

    toggle.addEventListener('click', function () {
      const isOpen = toggle.getAttribute('aria-expanded') === 'true';
      toggle.setAttribute('aria-expanded', String(!isOpen));
      menu.classList.toggle('open');
    });

    menu.querySelectorAll('a').forEach(function (link) {
      link.addEventListener('click', function () {
        toggle.setAttribute('aria-expanded', 'false');
        menu.classList.remove('open');
      });
    });
  }

  /* --- FAQ scroll-position fix --- */
  // When a <details> toggles open/closed the page height changes and the
  // browser's scroll-anchoring can shift the viewport, making it look like
  // the answer expands "upward". We counteract this by pinning the clicked
  // <summary> to its viewport position across the toggle.
  function initFaqScrollFix() {
    document.querySelectorAll('.faq-question').forEach(function (summary) {
      summary.addEventListener('click', function () {
        const topBefore = summary.getBoundingClientRect().top;
        requestAnimationFrame(function () {
          const topAfter = summary.getBoundingClientRect().top;
          const drift = topAfter - topBefore;
          if (drift) {
            window.scrollBy({ top: drift, behavior: 'instant' });
          }
        });
      });
    });
  }

  /* --- AOS Init --- */
  function initAOS() {
    if (typeof AOS === 'undefined') return;
    const prefersReducedMotion = window.matchMedia('(prefers-reduced-motion: reduce)').matches;
    if (prefersReducedMotion) return;
    AOS.init({
      duration: 600,
      easing: 'ease-out-cubic',
      once: true,
      offset: 50
    });

  }

  /* --- Boot --- */
  document.addEventListener('DOMContentLoaded', function () {
    initCountdown();
    initNavScroll();
    initMobileNav();
    initFaqScrollFix();
    initAOS();
  });
})();
