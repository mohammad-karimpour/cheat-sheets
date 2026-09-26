let Tione = document.getElementById('oneTitle')
  


document.addEventListener('DOMContentLoaded', function () {
  // ارسال پیام به content.js برای دریافت URL صفحه
  chrome.runtime.sendMessage({ action: 'getUrl' }, function(response) {
    Tione.innerHTML = response
  });
});
