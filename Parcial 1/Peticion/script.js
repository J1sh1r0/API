document.getElementById('fetchImages').addEventListener('click', fetchImages);

function fetchImages() {
    const url = 'https://picsum.photos/v2/list?page=2&limit=9';

    fetch(url)
        .then(response => response.json())
        .then(data => {
            const gallery = document.getElementById('gallery');
            gallery.innerHTML = ''; // Limpiar el contenido anterior

            data.forEach(image => {
                const imgContainer = document.createElement('div');
                imgContainer.classList.add('image-container');

                imgContainer.innerHTML = `
                    <img src="${image.download_url}" alt="Imagen aleatoria">
                `;

                gallery.appendChild(imgContainer);
            });
        })
        .catch(error => console.error('Error al obtener las imágenes:', error));
}
