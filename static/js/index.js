function showCategory(category) {
    const categoryBtns = document.querySelectorAll('.pro_h1');
    const categoryDivs = document.querySelectorAll('.pro_div > div');

    categoryBtns.forEach(btn => {
        if (btn.textContent.trim() === category) {
            if (category === 'ALL' && btn.classList.contains('active')) {
                return;
            }
            btn.classList.add('active');
        } else {
            btn.classList.remove('active');
        }
    });

    categoryDivs.forEach(div => {
        if (div.previousElementSibling.textContent.trim() === category) {
            div.classList.add('active');
        } else {
            div.classList.remove('active');
        }
    });

    const products = document.querySelectorAll('.product');
    products.forEach(product => {
        if (category === 'ALL' || product.classList.contains(category)) {
            product.style.display = 'block';
        } else {
            product.style.display = 'none';
        }
    });
  }

//like
document.addEventListener('DOMContentLoaded', () => {
    function setupLikeButton(buttonId, iconId, countId, likeUrl) {
        const likeButton = document.getElementById(buttonId);
        const likeIcon = document.getElementById(iconId);
        const likeCount = document.getElementById(countId);

        if (!likeButton || !likeIcon || !likeCount) return;

        likeButton.addEventListener('click', (event) => {
            event.preventDefault();

            fetch(likeUrl, {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/x-www-form-urlencoded',
                    'X-CSRFToken': getCookie('csrftoken'),
                },
                body: new URLSearchParams({
                    'csrfmiddlewaretoken': getCookie('csrftoken'),
                }),
            })
            .then(response => response.json())
            .then(data => {
                if (data.liked) {
                    likeIcon.src = "/static/images/free-icon-heart-2107845.png";
                } else {
                    likeIcon.src = "/static/images/free-icon-heart-shape-outline-25424.png";
                }
                likeCount.textContent = data.likes_count;
            })
            .catch(error => console.error('Error:', error));
        });
    }

    document.querySelectorAll('[id^="like-button-"]').forEach(button => {
        const postId = button.id.split('-').pop();
        const likeButtonId = `like-button-${postId}`;
        const likeIconId = `like-icon-${postId}`;
        const likeCountId = `like-count-${postId}`;
        const likeUrl = button.dataset.url;

        setupLikeButton(likeButtonId, likeIconId, likeCountId, likeUrl);
    });

    function getCookie(name) {
        let cookieValue = null;
        if (document.cookie && document.cookie !== '') {
            const cookies = document.cookie.split(';');
            for (let i = 0; i < cookies.length; i++) {
                const cookie = cookies[i].trim();
                if (cookie.substring(0, name.length + 1) === (name + '=')) {
                    cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                    break;
                }
            }
        }
        return cookieValue;
    }
});

// products
document.addEventListener('DOMContentLoaded', () => {
    fetch('/api/products/')
        .then(response => response.json())
        .then(data => {
            const productsContainer = document.getElementById('products-container');

            data.forEach(product => {
                const button = document.createElement('button');
                button.className = 'add-to-cart';
                button.setAttribute('data-product-id', product.id);
                button.setAttribute('data-product-name', product.title);
                button.textContent = `Добавить ${product.title}`;
                button.addEventListener('click', () => {
                    addToCart(product.id);
                });
                productsContainer.appendChild(button);
            });
        })
        .catch(error => {
            console.error('Ошибка при загрузке данных:', error);
        });
});

function addToCart(productId) {
    fetch('/add-to-cart/', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
            'X-CSRFToken': getCookie('csrftoken')
        },
        body: JSON.stringify({ product_id: productId })
    })
    .then(response => response.json())
    .then(data => {
        if (data.status === 'success') {
            alert('Товар добавлен в корзину!');
            window.location.href = 'bag.html';
        } else {
            alert('Ошибка при добавлении товара в корзину.');
        }
    })
    .catch(error => {
        console.error('Ошибка:', error);
    });
}

function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        const cookies = document.cookie.split(';');
        for (let i = 0; i < cookies.length; i++) {
            const cookie = cookies[i].trim();
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}
