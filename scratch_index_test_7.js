
    function redirectHomeSearch() {
      const input = document.getElementById('smart-search-input');
      const val = input ? input.value.trim() : '';
      if (val) {
        window.location.href = '/ask.html?q=' + encodeURIComponent(val);
      }
    }
    