function runScript() {
  var xhr = new XMLHttpRequest();
  xhr.open('GET', 'script.py', true);
  xhr.onload = function() {
    if (xhr.status === 200) {
      document.getElementById('output').innerHTML = xhr.responseText;
    } else {
      alert('Error: ' + xhr.statusText);
    }
  };
  xhr.onerror = function() {
    alert('Network Error');
  };
  xhr.send();
}
