document.addEventListener('DOMContentLoaded', function() {
    const favoriteButtons = document.querySelectorAll('.favorite-button');
    favoriteButtons.forEach(button => {
        const icon = button.querySelector('.material-icons');
        const isFavorited = icon.innerText === 'favorite';
        if (isFavorited) {
            icon.style.color = 'red';
        } else {
            icon.style.color = 'white';
        }
        button.addEventListener('click', function(event) {
            event.preventDefault();
            const recipeId = this.getAttribute('data-recipe-id');
<<<<<<< HEAD
            const appName = this.getAttribute('appName');
            fetch(`/${appName}/${recipeId}/toggle_favorite/`, {
                method: 'POST',headers: {'X-CSRFToken': csrfToken,'Content-Type': 'application/json'}})
            .then(response => response.json()).then(data => {
=======
            const appName = this.getAttribute('data-app-name');
            fetch(`/${appName}/${recipeId}/toggle_favorite/`, {
                method: 'POST',
                headers: {
                    'X-CSRFToken': csrfToken,
                    'Content-Type': 'application/json'
                }
            })
            .then(response => response.json())
            .then(data => {
>>>>>>> new-feature
                const icon = this.querySelector('.material-icons');
                if (data.is_favorited) {
                    icon.innerText = 'favorite';
                    icon.style.color = 'red';
                } else {
                    icon.innerText = 'favorite_border';
                    icon.style.color = 'white';
                }
            })
            .catch(error => console.error('Error:', error));
        });
    });
});

window.addEventListener('pageshow', function(event) {
    if (event.persisted) {
        window.location.reload();
    }
});