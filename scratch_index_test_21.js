
    document.addEventListener('DOMContentLoaded', function() {
      document.querySelectorAll('.nav-tab-dropdown').forEach(function(dd) {
        var closeTimer;
        dd.addEventListener('mouseenter', function() {
          clearTimeout(closeTimer);
          document.querySelectorAll('.nav-tab-dropdown').forEach(function(other) {
            if (other !== dd) other.classList.remove('open');
          });
          dd.classList.add('open');
        });
        dd.addEventListener('mouseleave', function() {
          closeTimer = setTimeout(function() {
            dd.classList.remove('open');
          }, 300);
        });
      });
    });
  