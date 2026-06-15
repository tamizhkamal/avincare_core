// Google Translate Implementation
function googleTranslateElementInit() {
    console.log('Initializing Google Translate...');
    new google.translate.TranslateElement({
        pageLanguage: 'en',
        includedLanguages: 'ta,en,ar,fr',
        layout: google.translate.TranslateElement.InlineLayout.SIMPLE,
        autoDisplay: false
    }, 'google_translate_element');
}

function changeLanguage(lang) {
    console.log('Changing language to:', lang);
    
    // Wait for Google Translate to load
    const checkAndChange = () => {
        const selectElement = document.querySelector('.goog-te-combo');
        if (selectElement) {
            console.log('Found Google Translate select element');
            selectElement.value = lang;
            selectElement.dispatchEvent(new Event('change'));
            console.log('Language changed to:', lang);
        } else {
            console.log('Google Translate not ready, retrying...');
            setTimeout(checkAndChange, 1000);
        }
    };
    
    // Start checking after a short delay
    setTimeout(checkAndChange, 500);
}

// Alternative translation using browser's built-in translation (if available)
function translateWithBrowser(lang) {
    if ('translation' in navigator && 'translate' in navigator.translation) {
        navigator.translation.translate({
            sourceLanguage: 'en',
            targetLanguage: lang,
            targetScope: 'page'
        });
        return true;
    }
    return false;
}

// Fallback: Simple language switching with stored translations
const translations = {
    'ta': {
        'Home': 'முகப்பு',
        'About': 'பற்றி',
        'Responsibility': 'பொறுப்பு',
        'Products': 'தயாரிப்புகள்',
        'Who We Are': 'நாங்கள் யார்',
        'Contact': 'தொடர்பு',
        'Language': 'மொழி'
    },
    'ar': {
        'Home': 'الصفحة الرئيسية',
        'About': 'حول',
        'Responsibility': 'المسؤولية',
        'Products': 'المنتجات',
        'Who We Are': 'من نحن',
        'Contact': 'اتصل',
        'Language': 'اللغة'
    },
    'fr': {
        'Home': 'Accueil',
        'About': 'À propos',
        'Responsibility': 'Responsabilité',
        'Products': 'Produits',
        'Who We Are': 'Qui nous sommes',
        'Contact': 'Contact',
        'Language': 'Langue'
    }
};

function simpleTranslate(lang) {
    const trans = translations[lang];
    if (trans) {
        // Translate navigation links
        document.querySelectorAll('.nav-link').forEach(link => {
            const text = link.textContent.trim();
            if (trans[text]) {
                link.textContent = trans[text];
            }
        });
    }
}
