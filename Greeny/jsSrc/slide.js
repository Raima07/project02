    console.log("Script loaded!");

    const pages = [
      { id: 1, content: 'Page 1', color: 'bg-black' },
      { id: 2, content: 'Page 2', color: 'bg-black' },
      { id: 3, content: 'Page 3', color: 'bg-black' },
      { id: 4, content: 'Page 4', color: 'bg-black' },
      { id: 5, content: 'Page 5', color: 'bg-black' }
    ];

    const pagesWrapper = document.getElementById('pages-wrapper');
    const pageContainer = document.getElementById('pageContainer');
    let currentPageIndex = 0;
    let timeoutId;

    function getNextPageIndex() {
      return (currentPageIndex + 1) % pages.length;
    }

    function getPrevPageIndex() {
      return (currentPageIndex - 1 + pages.length) % pages.length;
    }

    function createPages() {
      pagesWrapper.innerHTML = '';

      pages.forEach((page, index) => {
        const pageElement = document.createElement('div');
        pageElement.id = `page-${page.id}`;
        pageElement.className = `page ${page.color}`;

        if (page.id === 1) {
          pageElement.innerHTML = `
            <div class="relative w-full h-full p-6">
              <h3 class="absolute top-4 left-4 text-xl font-semibold text-green-200">About Us</h3>
              <div class="flex flex-col justify-center items-center h-full text-center px-4">
                <h1 class="text-3xl font-bold mb-4 text-white">🌿 Welcome to Our Plant & Garden Website!</h1>
                <p class="text-lg leading-relaxed max-w-md text-lime-200">
                  This website is a college project created with a passion for nature and technology. Our goal is to provide an interactive platform where users can explore various plants, learn about gardening tips, and understand how to take care of their green companions.
                </p>
              </div>
            </div>
          `;
        }
        if (page.id === 2) {
          pageElement.innerHTML = `
            <div class="relative w-full h-full p-6 text-white">
              <!-- Top-left heading -->
              <h3 class="absolute top-4 left-4 text-xl font-semibold text-green-200">About Us</h3>
        
              <!-- Centered content -->
              <div class="flex flex-col justify-center items-center h-full text-center px-4">
                <h1 class="text-3xl font-bold mb-4 text-white">🌱 Our Mission</h1>
                <p class="text-lg leading-relaxed max-w-md text-lime-200">
                  We aim to promote awareness about plants, their benefits, and sustainable gardening practices. Through this project, we hope to encourage people to embrace greenery and create their own little gardens, whether indoors or outdoors.
                </p>
              </div>
            </div>
          `;
        }
        if (page.id === 3) {
          pageElement.innerHTML = `
            <div class="relative w-full h-full p-6 text-white">
              <!-- Top-left heading -->
              <h3 class="absolute top-4 left-4 text-xl font-semibold text-green-200">About Us</h3>
        
              <!-- Centered content -->
              <div class="flex flex-col justify-center items-center h-full text-center px-4">
                <h1 class="text-3xl font-bold mb-4 text-white">🌍 Meet the Team</h1>
                <p class="text-lg text-lime-200 max-w-md mb-4">
                  Our project is developed by a group of enthusiastic students who share a common love for nature and web development. Each team member played a crucial role in bringing this website to life:
                </p>
                <ul class="text-green-300 text-base space-y-1">
                  <li>Ankita Chakraborty</li>
                  <li>Ankhi Sharma</li>
                  <li>Pallabi Dutta</li>
                  <li>Raima Banerjee</li>
                  <li>Rajatava Saha</li>
                </ul>
              </div>
            </div>
          `;
        }
        if (page.id === 4) {
          pageElement.innerHTML = `
            <div class="relative w-full h-full p-6 text-white">
              <!-- Top-left heading -->
              <h3 class="absolute top-4 left-4 text-xl font-semibold text-green-200">About Us</h3>
        
              <!-- Centered content -->
              <div class="flex flex-col justify-center items-center h-full text-center px-6">
                <h1 class="text-3xl font-bold mb-4 text-white">💡 Technologies Used</h1>
                <p class="text-lg text-lime-200 max-w-xl mb-6">
                  To build this website, we utilized modern web development technologies, including:
                </p> 
              </div>
            </div>
          `;
        }
        if (page.id === 5) {
          pageElement.innerHTML = `
            <div class="relative w-full h-full p-6 text-white">
              <!-- Top-left heading -->
              <h3 class="absolute top-4 left-4 text-xl font-semibold text-green-200">About Us</h3>
        
              <!-- Main Content -->
              <div class="flex flex-col justify-center items-center h-full text-center px-6 space-y-6">
                <!-- Acknowledgments Section -->
                <div>
                  <h1 class="text-3xl font-bold mb-3 text-white">📍 Acknowledgments</h1>
                  <p class="text-lg text-lime-200 max-w-xl">
                    We would like to extend our heartfelt gratitude to our professors and mentors for guiding us throughout this project. Special thanks to the online resources and communities that helped us overcome challenges and enhance our learning experience.
                  </p>
                </div>
        
                <!-- Thank You Section -->
                <div>
                  <h1 class="text-3xl font-bold mb-3 text-white">🌱 Thank You!</h1>
                  <p class="text-lg text-lime-200 max-w-xl">
                    Thank you for visiting our website! We hope you find it informative and inspiring. ✨
                  </p>
                </div>
              </div>
            </div>
        `;
        }





        if (index === currentPageIndex) {
          pageElement.classList.add('current');
        } else if (index === getNextPageIndex()) {
          pageElement.classList.add('next');
        } else if (index === getPrevPageIndex()) {
          pageElement.classList.add('prev');
        } else {
          pageElement.classList.add('hidden-page');
        }

        pagesWrapper.appendChild(pageElement);
      });
    }

    function flipToNextPage() {
      const currentPage = document.getElementById(`page-${pages[currentPageIndex].id}`);
      const nextPage = document.getElementById(`page-${pages[getNextPageIndex()].id}`);

      // Remove all position classes
      currentPage.className = currentPage.className.replace(/(current|next|prev|hidden-page)/g, '').trim() + ' page';
      nextPage.className = nextPage.className.replace(/(current|next|prev|hidden-page)/g, '').trim() + ' page';

      // Add animation classes
      currentPage.classList.add('flipping-prev');
      nextPage.classList.add('flipping-current');

      // After animation, update the positions
      timeoutId = setTimeout(() => {
        // Update currentPageIndex
        currentPageIndex = getNextPageIndex();

        // Reset all pages
        document.querySelectorAll('.page').forEach((pageElem, index) => {
          pageElem.className = pageElem.className.replace(/(current|next|prev|hidden-page|flipping-\w+)/g, '').trim() + ' page';

          if (index === currentPageIndex) {
            pageElem.classList.add('current');
          } else if (index === getNextPageIndex()) {
            pageElem.classList.add('next');
          } else if (index === getPrevPageIndex()) {
            pageElem.classList.add('prev');
          } else {
            pageElem.classList.add('hidden-page');
          }
        });

        // Schedule the next flip
        timeoutId = setTimeout(flipToNextPage, 3000); // Set delay between flips (in ms)
      }, 500); // This should match the animation duration
    }

    // Initialize
    createPages();
    timeoutId = setTimeout(flipToNextPage, 3000); // Start the flipping after 3 seconds

    // Hover effects to pause flipping on mouseenter and resume on mouseleave
    pageContainer.addEventListener('pointerenter', () => {
      clearTimeout(timeoutId);
    });

    pageContainer.addEventListener('pointerleave', () => {
      timeoutId = setTimeout(flipToNextPage, 3000); // Resume flipping after hover
    });

    // Touch events for mobile devices (to prevent the animation from stopping on touch)
    pageContainer.addEventListener('touchstart', () => {
      clearTimeout(timeoutId);
    }, { passive: true });

    pageContainer.addEventListener('touchend', () => {
      timeoutId = setTimeout(flipToNextPage, 3000); // Resume flipping after touch
    }, { passive: true });