// CodeForge — Interactivity
(function () {
  const $ = (sel, el = document) => el.querySelector(sel);
  const $$ = (sel, el = document) => Array.from(el.querySelectorAll(sel));

  // Year in footer
  $('#year').textContent = new Date().getFullYear();

  // Countdown
  const hero = $('.hero');
  const dateAttr = hero?.getAttribute('data-event-date');
  let targetDate;
  if (dateAttr) {
    const d = new Date(dateAttr);
    targetDate = isNaN(d.getTime()) ? null : d;
  }
  if (!targetDate) {
    const now = new Date();
    targetDate = new Date(now.getFullYear(), now.getMonth(), now.getDate() + 30, 9, 0, 0);
  }

  function updateCountdown() {
    const now = new Date();
    const diff = Math.max(0, targetDate - now);
    const s = Math.floor(diff / 1000);
    const d = Math.floor(s / 86400);
    const h = Math.floor((s % 86400) / 3600);
    const m = Math.floor((s % 3600) / 60);
    const sec = s % 60;
    setText('#days', d);
    setText('#hours', h);
    setText('#minutes', m);
    setText('#seconds', sec);
  }
  function setText(id, val) {
    const el = $(id);
    if (el) el.textContent = String(val).padStart(2, '0');
  }
  updateCountdown();
  setInterval(updateCountdown, 1000);

  // Scroll reveal
  const revealEls = $$('.reveal');
  const io = new IntersectionObserver((entries) => {
    for (const e of entries) {
      if (e.isIntersecting) {
        e.target.classList.add('reveal-visible');
        io.unobserve(e.target);
      }
    }
  }, { threshold: 0.12 });
  revealEls.forEach((el) => io.observe(el));

  // Timeline generation
  const timeline = $('#timeline');
  const schedule = [
    { time: 'Day 1 — 9:00', title: 'Check-in & Breakfast', desc: 'Grab your badge, fuel up, and meet peers.' },
    { time: 'Day 1 — 10:00', title: 'Opening Ceremony', desc: 'Themes, rules, and lightning inspiration.' },
    { time: 'Day 1 — 11:00', title: 'Hacking Starts', desc: 'Find your flow. Mentors on deck.' },
    { time: 'Day 1 — 14:00', title: 'Workshop: Rapid Prototyping', desc: 'Ship faster with expert tips.' },
    { time: 'Day 1 — 19:00', title: 'Dinner + Checkpoint', desc: 'Progress sync and snacks.' },
    { time: 'Day 2 — 09:30', title: 'Standup + Mentors', desc: 'Get feedback and unblock.' },
    { time: 'Day 2 — 13:00', title: 'Submission Freeze', desc: 'Code down. Prep your pitch.' },
    { time: 'Day 2 — 14:00', title: 'Demos', desc: 'Showtime on the neon stage.' },
    { time: 'Day 2 — 17:00', title: 'Awards + Close', desc: 'Celebrate winners and community.' },
  ];
  if (timeline) {
    const frag = document.createDocumentFragment();
    schedule.forEach((item) => {
      const el = document.createElement('div');
      el.className = 'tl-item';
      el.innerHTML = `
        <span class="tl-dot" aria-hidden="true"></span>
        <div class="tl-time">${item.time}</div>
        <div class="tl-title">${item.title}</div>
        <div class="tl-desc">${item.desc}</div>
      `;
      frag.appendChild(el);
    });
    timeline.appendChild(frag);
  }

  // Registration form
  const form = $('#regForm');
  const formMsg = $('#formMsg');
  if (form) {
    form.addEventListener('submit', (e) => {
      e.preventDefault();
      const data = new FormData(form);
      const team = (data.get('teamName') || 'your team').toString();
      formMsg.textContent = `🔥 Registered! See you at CodeForge, ${team}.`;
      form.reset();
      form.classList.add('shake');
      setTimeout(() => form.classList.remove('shake'), 500);
    });
  }

  // Live updates
  const updatesEl = $('#updatesFeed');
  const initialUpdates = [
    'Venue opens — check-in begins.',
    'Wi‑Fi: CODEFORGE / Pass: forge2025',
    'Mentor desk live at 11:00.',
    'Workshop slides available on dashboard.',
    'Food trucks parked on the east lot.',
  ];
  const laterUpdates = [
    'Submission portal is now live.',
    'Don’t forget to hydrate — water stations refilled.',
    'Lightning talk in 10 minutes at Stage B.',
    'Judges arriving — rehearse your demo!',
    'Raffle at 16:30 — keep your badge handy.',
    'Afterparty playlist requests open in Slack.',
  ];

  function addUpdate(msg) {
    const li = document.createElement('li');
    li.className = 'update reveal reveal-visible';
    const time = new Date().toLocaleTimeString([], { hour: '2-digit', minute: '2-digit' });
    li.innerHTML = `<div class="meta">${time}</div><p class="msg">${msg}</p>`;
    updatesEl.prepend(li);
    // Keep feed concise
    while (updatesEl.children.length > 6) updatesEl.lastElementChild?.remove();
  }

  if (updatesEl) {
    initialUpdates.forEach((u, i) => setTimeout(() => addUpdate(u), i * 200));
    let idx = 0;
    setInterval(() => {
      addUpdate(laterUpdates[idx % laterUpdates.length]);
      idx++;
    }, 8000);
  }
})();

