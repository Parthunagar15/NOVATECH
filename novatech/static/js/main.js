/* ============================================================
   NOVATECH — MAIN JS
   ============================================================ */
document.addEventListener('DOMContentLoaded', () => {

  // ── NAVBAR SCROLL SHRINK ──────────────────────────────────
  window.addEventListener('scroll', () => {
    document.body.classList.toggle('scrolled', window.scrollY > 40);
  });

  // ── TOAST SYSTEM ──────────────────────────────────────────
  // Reads data-toast-msg / data-toast-type attributes injected by Django
  // on page load (set via messages framework).
  const toastEl = document.getElementById('toast');

  function showToast(message, type = 'info') {
    if (!toastEl) return;
    toastEl.textContent = message;
    toastEl.className = 'toast toast-' + type;
    // Force reflow so transition fires even if toast was already visible
    void toastEl.offsetWidth;
    toastEl.classList.add('show');
    setTimeout(() => toastEl.classList.remove('show'), 3200);
  }

  // Auto-show toast if Django injected one via <body> attributes
  if (toastEl) {
    const msg  = document.body.dataset.toastMsg;
    const type = document.body.dataset.toastType || 'info';
    if (msg) showToast(msg, type);
  }

  // Also expose globally so inline scripts can call it
  window.showToast = showToast;

  // ── PASSWORD TOGGLE (login + signup) ──────────────────────
  document.querySelectorAll('.toggle-pass').forEach(btn => {
    btn.addEventListener('click', () => {
      const input = btn.closest('.input-wrap').querySelector('input');
      const isHidden = input.type === 'password';
      input.type = isHidden ? 'text' : 'password';
      btn.textContent = isHidden ? '🙈' : '👁';
    });
  });

  // ── REAL-TIME PASSWORD STRENGTH (signup only) ────────────
  const pwInput      = document.getElementById('id_password');
  const strengthBar  = document.getElementById('strength-bar');
  const strengthLabel= document.getElementById('strength-label');

  if (pwInput && strengthBar) {
    pwInput.addEventListener('input', () => {
      const pw = pwInput.value;
      if (!pw) {
        strengthBar.innerHTML = '<div class="strength-seg"></div>'.repeat(3);
        strengthLabel.textContent = '';
        strengthLabel.className = 'strength-label';
        return;
      }

      let score = 0;
      if (pw.length >= 6)                              score++;
      if (pw.length >= 8)                              score++;
      if (/[A-Z]/.test(pw) && /[a-z]/.test(pw))       score++;
      if (/\d/.test(pw))                               score++;
      if (/[^A-Za-z0-9]/.test(pw))                    score++;

      let level, label, cls;
      if      (score <= 2) { level = 1; label = 'Weak';   cls = 'weak'; }
      else if (score <= 3) { level = 2; label = 'Fair';   cls = 'fair'; }
      else                 { level = 3; label = 'Strong'; cls = 'good'; }

      strengthBar.innerHTML = [0,1,2].map(i =>
        `<div class="strength-seg ${i < level ? cls : ''}"></div>`
      ).join('');

      strengthLabel.textContent = 'Strength: ' + label;
      strengthLabel.className   = 'strength-label ' + cls;
    });
  }

  // ── CONTACT "SEND ANOTHER" BUTTON ─────────────────────────
  // The success overlay contains a button that reloads the contact page
  const sendAnother = document.getElementById('send-another');
  if (sendAnother) {
    sendAnother.addEventListener('click', () => {
      window.location.href = '/contact/';
    });
  }

});
