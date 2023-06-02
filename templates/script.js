document.getElementById("myForm").addEventListener("submit", function(event) {
    event.preventDefault();
    const name = document.getElementById("name").value;
    const usn = document.getElementById("usn").value;
    const url = `index2.html?name=${encodeURIComponent(name)}&usn=${encodeURIComponent(usn)}`;
    window.location.href = url;
  
  
    // JavaScript code to handle form submission
    document.getElementById('myForm').addEventListener('submit', function(event) {
      var nameValue = document.getElementById('name').value;
      var usnValue = document.getElementById('usn').value;
  
      if (!nameValue || !usnValue) {
        event.preventDefault(); // Prevent form submission
        alert('Please fill in both Name and USN fields.');
      }
   

    });
  
});