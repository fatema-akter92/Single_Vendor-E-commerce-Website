// Main JavaScript for interactive frontend operations

document.addEventListener('DOMContentLoaded', function () {
    // Auto-dismiss alerts after 4 seconds
    const alerts = document.querySelectorAll('.alert-dismissible');
    alerts.forEach(function (alert) {
        setTimeout(function () {
            const bsAlert = new bootstrap.Alert(alert);
            bsAlert.close();
        }, 4000);
    });

    // Quantity Increment / Decrement Buttons
    const qtyBtnMinus = document.querySelectorAll('.btn-qty-minus');
    const qtyBtnPlus = document.querySelectorAll('.btn-qty-plus');

    qtyBtnMinus.forEach(btn => {
        btn.addEventListener('click', function () {
            const input = this.closest('.input-group').querySelector('.qty-input');
            let currentVal = parseInt(input.value) || 1;
            if (currentVal > 1) {
                input.value = currentVal - 1;
            }
        });
    });

    qtyBtnPlus.forEach(btn => {
        btn.addEventListener('click', function () {
            const input = this.closest('.input-group').querySelector('.qty-input');
            let currentVal = parseInt(input.value) || 1;
            let maxVal = parseInt(input.getAttribute('max')) || 99;
            if (currentVal < maxVal) {
                input.value = currentVal + 1;
            }
        });
    });

    // Checkout Form Validation
    const checkoutForm = document.getElementById('checkoutForm');
    if (checkoutForm) {
        checkoutForm.addEventListener('submit', function (e) {
            const nameInput = document.querySelector('input[name="name"]');
            const phoneInput = document.querySelector('input[name="phone"]');
            const addressInput = document.querySelector('textarea[name="address"]');

            if (!nameInput.value.trim() || !phoneInput.value.trim() || !addressInput.value.trim()) {
                e.preventDefault();
                alert('Please complete all required fields (Name, Phone Number, and Address).');
            }
        });
    }
});
