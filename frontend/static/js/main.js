document.addEventListener('DOMContentLoaded', function () {
    /* ── Intro video logic - skip layer + native video controls ───────── */
    const introOverlay = document.getElementById('introVideoOverlay');
    const introVideo = document.getElementById('introVideo');
    const introVideoSkipLayer = document.getElementById('introVideoSkipLayer');

    const introVideoSource = introVideo ? introVideo.querySelector('source') : null;
    const introVideoVersion = introVideoSource ? introVideoSource.getAttribute('src') : 'intro-video';
    const INTRO_VIDEO_KEY = 'introVideoPlayed:' + introVideoVersion;
    const shouldShowIntro = introOverlay && introVideo && !sessionStorage.getItem(INTRO_VIDEO_KEY);

    if (introOverlay && introVideo) {
        if (shouldShowIntro) {
            document.body.classList.add('intro-playing');

            let introClosed = false;

            function showHomePage() {
                if (introClosed) return;

                introClosed = true;

                introOverlay.classList.add('hide-intro');
                document.body.classList.remove('intro-playing');

                setTimeout(function () {
                    introOverlay.style.display = 'none';
                    introVideo.pause();
                }, 550);

                sessionStorage.setItem(INTRO_VIDEO_KEY, '1');
            }

            introVideo.addEventListener('loadedmetadata', function () {
                introVideo.controls = true;
            });

            introVideo.addEventListener('canplay', function () {
                introVideo.controls = true;

                introVideo.play().catch(function () {
                    // Autoplay may be blocked in rare cases.
                });
            });

            introVideo.addEventListener('ended', function () {
                showHomePage();
            });

            introVideo.addEventListener('error', function () {
                showHomePage();
            });

            /*
              Important:
              The skip layer sits above the video middle/side area.
              It does NOT cover the bottom native video controls/progress bar.
              So:
              - Touch/click middle video area = skip intro and show homepage
              - Touch/drag progress bar = video seek works normally
            */
            if (introVideoSkipLayer) {
                introVideoSkipLayer.addEventListener('click', function (event) {
                    event.preventDefault();
                    event.stopPropagation();
                    showHomePage();
                });

                introVideoSkipLayer.addEventListener('touchstart', function (event) {
                    event.preventDefault();
                    event.stopPropagation();
                    showHomePage();
                }, { passive: false });
            }

        } else {
            introOverlay.style.display = 'none';
            document.body.classList.remove('intro-playing');

            if (introVideo) {
                introVideo.pause();
            }
        }
    }

    /* ── Navbar scroll effect ─────────────────────────────── */
    const nav = document.getElementById('mainNav');

    if (nav) {
        window.addEventListener('scroll', function () {
            nav.classList.toggle('scrolled', window.scrollY > 40);
        }, { passive: true });
    }

    /* ── Active nav link ──────────────────────────────────── */
    const currentPath = window.location.pathname;

    document.querySelectorAll('.nav-links a:not(.nav-cta)').forEach(function (link) {
        const href = link.getAttribute('href');

        if (href && (href === currentPath || (href !== '/' && currentPath.startsWith(href)))) {
            link.classList.add('nav-active');
        }
    });

    /* ── Scroll reveal ────────────────────────────────────── */
    const revealEls = document.querySelectorAll(
        '.stat-card, .track-card, .idea-card, .monument-card, .idea-track-section, ' +
        '.timeline-item, .info-card, .opportunity-card, .contact-card, ' +
        '.prize-card, .portrait-img, .legacy-img, .monument-img, .large-quote'
    );

    revealEls.forEach(function (el, i) {
        el.classList.add('reveal');

        const mod = i % 4;
        if (mod === 1) el.classList.add('reveal-delay-1');
        if (mod === 2) el.classList.add('reveal-delay-2');
        if (mod === 3) el.classList.add('reveal-delay-3');
        if (mod === 0 && i > 0) el.classList.add('reveal-delay-4');
    });

    if ('IntersectionObserver' in window) {
        const revealObserver = new IntersectionObserver(function (entries) {
            entries.forEach(function (entry) {
                if (entry.isIntersecting) {
                    entry.target.classList.add('visible');
                    revealObserver.unobserve(entry.target);
                }
            });
        }, { threshold: 0.1, rootMargin: '0px 0px -40px 0px' });

        revealEls.forEach(function (el) {
            revealObserver.observe(el);
        });
    } else {
        revealEls.forEach(function (el) {
            el.classList.add('visible');
        });
    }

    /* ── Animated counters ────────────────────────────────── */
    function animateCounter(el) {
        const target = parseInt(el.textContent.replace(/,/g, ''), 10);

        if (isNaN(target) || target === 0) return;

        let startTime = null;
        const duration = 1400;

        function step(timestamp) {
            if (!startTime) startTime = timestamp;

            const progress = Math.min((timestamp - startTime) / duration, 1);
            const eased = 1 - Math.pow(1 - progress, 3);

            el.textContent = Math.floor(eased * target).toLocaleString('en-IN');

            if (progress < 1) {
                requestAnimationFrame(step);
            } else {
                el.textContent = target.toLocaleString('en-IN');
            }
        }

        requestAnimationFrame(step);
    }

    const participateSection = document.querySelector('.participate-section');

    if (participateSection) {
        if ('IntersectionObserver' in window) {
            const participateObserver = new IntersectionObserver(function (entries) {
                entries.forEach(function (entry) {
                    if (entry.isIntersecting) {
                        participateSection.classList.add('participate-in-view');
                        participateObserver.unobserve(participateSection);
                    }
                });
            }, { threshold: 0.28, rootMargin: '0px 0px -80px 0px' });

            participateObserver.observe(participateSection);
        } else {
            participateSection.classList.add('participate-in-view');
        }
    }

    const statCounters = document.querySelectorAll('.stat-card h3');

    if ('IntersectionObserver' in window) {
        const counterObserver = new IntersectionObserver(function (entries) {
            entries.forEach(function (entry) {
                if (entry.isIntersecting) {
                    const cardIndex = Array.from(statCounters).indexOf(entry.target);
                    setTimeout(function () {
                        animateCounter(entry.target);
                    }, Math.max(cardIndex, 0) * 350);
                    counterObserver.unobserve(entry.target);
                }
            });
        }, { threshold: 0.5 });

        statCounters.forEach(function (el) {
            counterObserver.observe(el);
        });
    }

    /* ── Auto-dismiss flash messages ─────────────────────── */
    setTimeout(function () {
        document.querySelectorAll('.alert').forEach(function (alert) {
            alert.style.transition = 'opacity 0.5s ease, transform 0.5s ease';
            alert.style.opacity = '0';
            alert.style.transform = 'translateX(40px)';

            setTimeout(function () {
                alert.remove();
            }, 500);
        });
    }, 4500);

    /* ── Download toast messages ─────────────────────────── */
    document.querySelectorAll('[data-download-toast]').forEach(function (link) {
        link.addEventListener('click', function () {
            const message = link.getAttribute('data-download-toast') || 'File successfully downloaded';
            let container = document.querySelector('.messages-container');

            if (!container) {
                container = document.createElement('div');
                container.className = 'messages-container';
                document.body.appendChild(container);
            }

            const alert = document.createElement('div');
            alert.className = 'alert';
            alert.textContent = message;
            container.appendChild(alert);

            setTimeout(function () {
                alert.style.transition = 'opacity 0.5s ease, transform 0.5s ease';
                alert.style.opacity = '0';
                alert.style.transform = 'translateX(40px)';

                setTimeout(function () {
                    alert.remove();
                }, 500);
            }, 2600);
        });
    });

    /* ── Mobile hamburger menu ────────────────────────────── */
    const navToggle = document.getElementById('navToggle');
    const navLinks = document.getElementById('navLinks');

    if (navToggle && navLinks && nav) {
        navToggle.addEventListener('click', function (event) {
            event.stopPropagation();

            navLinks.classList.toggle('menu-open');
            navToggle.classList.toggle('active');

            const isOpen = navLinks.classList.contains('menu-open');
            navToggle.setAttribute('aria-expanded', isOpen ? 'true' : 'false');
        });

        document.querySelectorAll('.dropdown-toggle').forEach(function (toggle) {
            toggle.addEventListener('click', function (event) {
                if (window.innerWidth <= 900) {
                    event.preventDefault();
                    event.stopPropagation();

                    const parentDropdown = toggle.closest('.nav-dropdown');

                    document.querySelectorAll('.nav-dropdown').forEach(function (dropdown) {
                        if (dropdown !== parentDropdown) {
                            dropdown.classList.remove('dropdown-open');
                        }
                    });

                    if (parentDropdown) {
                        parentDropdown.classList.toggle('dropdown-open');
                    }
                }
            });
        });

        document.querySelectorAll('.nav-links a').forEach(function (link) {
            link.addEventListener('click', function () {
                if (window.innerWidth <= 900) {
                    navLinks.classList.remove('menu-open');
                    navToggle.classList.remove('active');
                    navToggle.setAttribute('aria-expanded', 'false');

                    document.querySelectorAll('.nav-dropdown').forEach(function (dropdown) {
                        dropdown.classList.remove('dropdown-open');
                    });
                }
            });
        });

        document.addEventListener('click', function (event) {
            if (window.innerWidth <= 900 && !nav.contains(event.target)) {
                navLinks.classList.remove('menu-open');
                navToggle.classList.remove('active');
                navToggle.setAttribute('aria-expanded', 'false');

                document.querySelectorAll('.nav-dropdown').forEach(function (dropdown) {
                    dropdown.classList.remove('dropdown-open');
                });
            }
        });

        window.addEventListener('resize', function () {
            if (window.innerWidth > 900) {
                navLinks.classList.remove('menu-open');
                navToggle.classList.remove('active');
                navToggle.setAttribute('aria-expanded', 'false');

                document.querySelectorAll('.nav-dropdown').forEach(function (dropdown) {
                    dropdown.classList.remove('dropdown-open');
                });
            }
        });
    }
});