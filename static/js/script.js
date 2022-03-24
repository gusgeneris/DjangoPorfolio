(function($) { // Begin jQuery
    $(function() { // DOM ready
        // If a link has a dropdown, add sub menu toggle.
        $('nav ul li a:not(:only-child)').click(function(e) {
            $(this).siblings('.nav-dropdown').toggle();
            // Close one dropdown when selecting another
            $('.nav-dropdown').not($(this).siblings()).hide();
            e.stopPropagation();
        });
        // Clicking away from dropdown will remove the dropdown class
        $('html').click(function() {
            $('.nav-dropdown').hide();
        });
        // Toggle open and close nav styles on click
        $('#nav-toggle').click(function() {
            $('nav ul').slideToggle();
        });
        // Hamburger to X toggle
        $('#nav-toggle').on('click', function() {
            this.classList.toggle('active');
        });
    }); // end DOM ready
})(jQuery); // end jQuery

// other theme mode

const boton = document.querySelector('#switch');
const configUser = document.body.className;
const localConfig = localStorage.getItem('tema');
console.log(localConfig)
if (localConfig === 'dark') {
    document.body.classList.toggle('dark-theme')
} else if (localConfig === 'light') {
    document.body.classList.toggle('light-theme')
}
boton.addEventListener('click', () => {
    let colorTema;
    if (configUser.match('btg-body')) {
        // Entramos con modo oscuro
        document.body.classList.toggle('light-theme')
        colorTema = document.body.classList.contains('light-theme') ? 'light' : 'dark'
        console.log(colorTema + ' modo oscuro')

    } else {
        document.body.classList.toggle('dark-theme')
        colorTema = document.body.classList.contains('dark-theme') ? 'dark' : 'light'
        console.log(colorTema + ' modo cla')
        console.log(configUser)
    }
    localStorage.setItem('tema', colorTema)
})