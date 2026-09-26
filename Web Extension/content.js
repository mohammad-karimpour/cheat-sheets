let currentUrl = document.getElementById('font-25');

// ارسال URL به popup
chrome.runtime.onMessage.addListener((message, sendResponse) => {
  if (message.action === 'getUrl') {
    sendResponse({ url: currentUrl });
  }
});

  