/* =============================================
   Cajsa & Filip — Wedding Website Scripts
   ============================================= */

(function () {
  'use strict';

  /* --- Countdown Timer --- */
  function initCountdown() {
    const weddingDate = new Date('2026-05-23T16:00:00+02:00');

    function update() {
      const now = new Date();
      const diff = weddingDate - now;

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

  /* --- Mobile Hamburger --- */
  function initMobileNav() {
    const toggle = document.querySelector('.nav-toggle');
    const menu = document.getElementById('nav-menu');
    if (!toggle || !menu) return;

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

  /* --- AOS Init --- */
  function initAOS() {
    if (typeof AOS === 'undefined') return;
    var prefersReducedMotion = window.matchMedia('(prefers-reduced-motion: reduce)').matches;
    if (prefersReducedMotion) return;
    AOS.init({
      duration: 800,
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
    initAOS();
  });
})();
