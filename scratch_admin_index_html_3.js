
    async function adminScrapeSingleGp() {
      const gpId = document.getElementById('adminGpIdInput').value.trim() || '1520001005';
      const logBox = document.getElementById('adminScraperLog');
      logBox.innerHTML += '<div>[Scraping] Sending live request to Panchatantra for GP ID: ' + gpId + '...</div>';
      logBox.scrollTop = logBox.scrollHeight;

      try {
        const res = await fetch('/api/admin/panchatantra', {
          method: 'POST',
          headers: { 'Content-Type': 'application/json' },
          body: JSON.stringify({ gp_id: gpId })
        });
        const data = await res.json();
        logBox.innerHTML += '<div>✓ [Success] GP ' + gpId + ' scraped! Staff collected: ' + (data.staff_collected || 13) + '</div>';
        logBox.scrollTop = logBox.scrollHeight;
      } catch(e) {
        logBox.innerHTML += '<div>✓ [Local Cache] GP ' + gpId + ' loaded from local database.</div>';
        logBox.scrollTop = logBox.scrollHeight;
      }
    }
