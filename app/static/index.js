 const name = document.querySelector('.name');
        const text = "Micheal Isaac";
        let index = 0;
        let forward = true; 

        function typeName() {
            if (forward) {
                // Type each letter
                name.textContent = text.slice(0, index + 1);
                index++;
                if (index === text.length) {
                    forward = false; // start deleting
                    setTimeout(typeName, 1000); // pause before deleting
                    return;
                }
            } else {
                // Delete each letter
                name.textContent = text.slice(0, index - 1);
                index--;
                if (index === 0) {
                    forward = true; 
                    setTimeout(typeName, 500); 
                    return;
                }
            }
            setTimeout(typeName, 150);
        }


        typeName();



function toggleModal() {
    const modal = document.getElementById('contactModal');
    if (modal.style.display === 'none' || modal.style.display === '') {
        modal.style.display = 'flex';
        document.body.style.overflow = 'hidden'; // Stop background scrolling
    } else {
        modal.style.display = 'none';
        document.body.style.overflow = 'auto'; // Re-enable background scrolling
    }
}
        
        // Close modal if clicking outside the white box
        window.onclick = function(event) {
            const modal = document.getElementById('contactModal');
            if (event.target == modal) { toggleModal(); }
        }


function markAttended(id, btn) {

    fetch(`/admin/contact/${id}/attend`, {
        method: "POST"
    })
    .then(res => res.json())
    .then(data => {

        if (data.success) {
            btn.innerText = "Attended";
            btn.classList.add("attended");
            btn.disabled = true;
        }
    })
    .catch(error => {
        console.error("Error:", error);
        alert("Something went wrong");
    });
}