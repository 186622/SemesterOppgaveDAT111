document.getElementById('dark-mode-toggle').addEventListener('click', function () {
    document.body.classList.toggle('light-mode');
});

const besokstallSelector = document.querySelector('#dag-velger');
const besokstallBilde = document.querySelector('#besokstall-img');
const besokstallParagraf = document.querySelector('#besokstall-tekst');

if (besokstallBilde) {
    let dayOfWeek = new Date().getDay();

    if (dayOfWeek < 1 || dayOfWeek > 5) dayOfWeek = 1;
    besokstallSelector.value = dayOfWeek;

    const velgBilde = (event) => {
        const val = event?.target?.value || dayOfWeek;

        let bildeUrl = '';
        let bildeAlt = '';
        let besokstallTekst = '';

        switch (parseInt(val)) {
            case 1:
                bildeUrl = 'besokstall_plot_Mandag.png';
                bildeAlt = 'Graf for mandag';
                besokstallTekst = 'Anbefalt tidsrom for besøk: mellom kl 9 - 10 og mellom kl 12 - 13.';
                break;
            case 2:
                bildeUrl = 'besokstall_plot_Tirsdag.png';
                bildeAlt = 'Graf for tirsdag';
                besokstallTekst = 'Anbefalt tidsrom for besøk: mellom kl 9 - 10, mellom kl 12 - 13 og mellom 17 - 18.';
                break;
            case 3:
                bildeUrl = 'besokstall_plot_Onsdag.png';
                bildeAlt = 'Graf for onsdag';
                besokstallTekst = 'Anbefalt tidsrom for besøk: mellom kl 9 - 10 og mellom kl 12 - 13.';
                break;
            case 4:
                bildeUrl = 'besokstall_plot_Torsdag.png';
                bildeAlt = 'Graf for torsdag';
                besokstallTekst = 'Anbefalt tidsrom for besøk: mellom kl 9 - 10, mellom kl 12 - 13 og mellom 17 - 18.';
                break;
            default:
                bildeUrl = 'besokstall_plot_Fredag.png';
                bildeAlt = 'Graf for fredag';
                besokstallTekst = 'Anbefalt tidsrom for besøk: mellom kl 9 - 10, mellom kl 12 - 13 og mellom 17 - 18.';
                break;
        }

        besokstallBilde.src = bildeUrl;
        besokstallBilde.alt = bildeAlt;
        besokstallParagraf.innerHTML = besokstallTekst;
    }

    besokstallSelector.addEventListener('change', velgBilde);
    velgBilde();
}