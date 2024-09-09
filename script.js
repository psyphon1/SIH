document.addEventListener("DOMContentLoaded", function() {
    const availableBedsElement = document.getElementById('available-beds');
    const occupiedBedsElement = document.getElementById('occupied-beds');
    const patientQueueElement = document.getElementById('patient-queue');

    let availableBeds = parseInt(availableBedsElement.textContent);
    let occupiedBeds = parseInt(occupiedBedsElement.textContent);

    document.getElementById('add-patient-btn').addEventListener('click', function() {
        const newPatient = prompt("Enter patient name:");
        if (newPatient) {
            const listItem = document.createElement('li');
            listItem.textContent = newPatient;
            patientQueueElement.appendChild(listItem);
        }
    });

    document.getElementById('admit-patient-btn').addEventListener('click', function() {
        if (availableBeds > 0 && patientQueueElement.children.length > 0) {
            availableBeds--;
            occupiedBeds++;

            availableBedsElement.textContent = availableBeds;
            occupiedBedsElement.textContent = occupiedBeds;

            patientQueueElement.removeChild(patientQueueElement.children[0]);
        } else {
            alert("No available beds or no patients in queue.");
        }
    });
});
