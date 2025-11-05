#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Programme de visualisation des spectres de modulation d'amplitude
TP Modulation d'amplitude - M1 SYSCOM
"""

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch

# Configuration matplotlib pour un affichage professionnel
plt.rcParams['font.size'] = 10
plt.rcParams['axes.grid'] = True
plt.rcParams['grid.alpha'] = 0.3


def tracer_spectre_DSB(f0=12000, fs=1500, A_amp=1.0, save=False):
    """
    Trace le spectre du signal modulé DSB (Double Side Band)

    M1(t) = (k*A0*B0/2) * [cos(2π(f0-fs)t) + cos(2π(f0+fs)t)]

    Paramètres:
    -----------
    f0 : float
        Fréquence de la porteuse en Hz (défaut: 12 kHz)
    fs : float
        Fréquence du signal modulant en Hz (défaut: 1.5 kHz)
    A_amp : float
        Amplitude normalisée (k*A0*B0/2)
    save : bool
        Sauvegarder la figure
    """
    # Fréquences des bandes latérales
    f_BLI = f0 - fs  # Bande Latérale Inférieure
    f_BLS = f0 + fs  # Bande Latérale Supérieure

    # Création de la figure
    fig, ax = plt.subplots(figsize=(12, 6))

    # Tracer les raies spectrales
    # Bande Latérale Inférieure
    ax.stem([f_BLI/1000], [A_amp], linefmt='b-', markerfmt='bo',
            basefmt='k-', label='Bande Latérale Inférieure (BLI)')

    # Bande Latérale Supérieure
    ax.stem([f_BLS/1000], [A_amp], linefmt='r-', markerfmt='ro',
            basefmt='k-', label='Bande Latérale Supérieure (BLS)')

    # Marquer la fréquence porteuse absente
    ax.axvline(f0/1000, color='gray', linestyle='--', alpha=0.5, linewidth=1.5)
    ax.text(f0/1000, A_amp*1.15, 'f₀ = 12 kHz\n(absente)',
            ha='center', va='bottom', fontsize=9, color='gray',
            bbox=dict(boxstyle='round,pad=0.5', facecolor='yellow', alpha=0.3))

    # Annotations
    ax.annotate(f'BLI\nf₀-fs = {f_BLI/1000:.1f} kHz\nAmplitude: {A_amp:.2f}',
                xy=(f_BLI/1000, A_amp), xytext=(f_BLI/1000-1.5, A_amp*1.3),
                bbox=dict(boxstyle='round,pad=0.5', facecolor='lightblue', alpha=0.7),
                arrowprops=dict(arrowstyle='->', connectionstyle='arc3,rad=0.3', color='blue'))

    ax.annotate(f'BLS\nf₀+fs = {f_BLS/1000:.1f} kHz\nAmplitude: {A_amp:.2f}',
                xy=(f_BLS/1000, A_amp), xytext=(f_BLS/1000+1.5, A_amp*1.3),
                bbox=dict(boxstyle='round,pad=0.5', facecolor='lightcoral', alpha=0.7),
                arrowprops=dict(arrowstyle='->', connectionstyle='arc3,rad=-0.3', color='red'))

    # Configuration des axes
    ax.set_xlabel('Fréquence (kHz)', fontsize=12, fontweight='bold')
    ax.set_ylabel('Amplitude normalisée', fontsize=12, fontweight='bold')
    ax.set_title('Spectre de M₁(t) - Modulation DSB (Double Side Band)\n' +
                 f'f₀ = {f0/1000} kHz, fs = {fs/1000} kHz',
                 fontsize=14, fontweight='bold', pad=20)
    ax.set_xlim(8, 16)
    ax.set_ylim(0, A_amp*1.6)
    ax.legend(loc='upper left', fontsize=10)
    ax.grid(True, alpha=0.3)

    # Ajouter un encadré explicatif
   
    

    plt.tight_layout()
    if save:
        plt.savefig('spectre_DSB.png', dpi=300, bbox_inches='tight')
        print("Figure sauvegardée: spectre_DSB.png")
    plt.show()


def tracer_spectre_AM(f0=12000, fs=1500, m=0.5, B0=1.0, save=False):
    """
    Trace le spectre du signal modulé AM (Amplitude Modulation)

    M2(t) = B0*cos(2πf0t) + (m*B0/2)*[cos(2π(f0-fs)t) + cos(2π(f0+fs)t)]

    Paramètres:
    -----------
    f0 : float
        Fréquence de la porteuse en Hz (défaut: 12 kHz)
    fs : float
        Fréquence du signal modulant en Hz (défaut: 1.5 kHz)
    m : float
        Indice de modulation (0 < m ≤ 1 recommandé)
    B0 : float
        Amplitude de la porteuse
    save : bool
        Sauvegarder la figure
    """
    # Fréquences
    f_porteuse = f0
    f_BLI = f0 - fs
    f_BLS = f0 + fs

    # Amplitudes
    A_porteuse = B0
    A_BL = (m * B0) / 2  # Amplitude des bandes latérales

    # Création de la figure
    fig, ax = plt.subplots(figsize=(12, 6))

    # Tracer les raies spectrales
    # Porteuse
    ax.stem([f_porteuse/1000], [A_porteuse], linefmt='g-', markerfmt='go',
            basefmt='k-', label='Porteuse (f₀)')

    # Bandes latérales
    ax.stem([f_BLI/1000], [A_BL], linefmt='b-', markerfmt='bo',
            basefmt='k-', label='BLI')
    ax.stem([f_BLS/1000], [A_BL], linefmt='r-', markerfmt='ro',
            basefmt='k-', label='BLS')

    # Annotations
    ax.annotate(f'Porteuse\nf₀ = {f_porteuse/1000} kHz\nAmplitude: {A_porteuse:.2f}',
                xy=(f_porteuse/1000, A_porteuse),
                xytext=(f_porteuse/1000, A_porteuse*1.25),
                bbox=dict(boxstyle='round,pad=0.5', facecolor='lightgreen', alpha=0.8),
                ha='center', fontsize=9, fontweight='bold')

    ax.annotate(f'BLI\n{f_BLI/1000:.1f} kHz\nA = {A_BL:.3f}',
                xy=(f_BLI/1000, A_BL), xytext=(f_BLI/1000-1.5, A_BL*2.5),
                bbox=dict(boxstyle='round,pad=0.4', facecolor='lightblue', alpha=0.7),
                arrowprops=dict(arrowstyle='->', color='blue'),
                fontsize=9)

    ax.annotate(f'BLS\n{f_BLS/1000:.1f} kHz\nA = {A_BL:.3f}',
                xy=(f_BLS/1000, A_BL), xytext=(f_BLS/1000+1.5, A_BL*2.5),
                bbox=dict(boxstyle='round,pad=0.4', facecolor='lightcoral', alpha=0.7),
                arrowprops=dict(arrowstyle='->', color='red'),
                fontsize=9)

    # Configuration des axes
    ax.set_xlabel('Fréquence (kHz)', fontsize=12, fontweight='bold')
    ax.set_ylabel('Amplitude normalisée', fontsize=12, fontweight='bold')
    ax.set_title(f'Spectre de M₂(t) - Modulation AM (Amplitude Modulation)\n' +
                 f'f₀ = {f0/1000} kHz, fs = {fs/1000} kHz, m = {m}',
                 fontsize=14, fontweight='bold', pad=20)
    ax.set_xlim(8, 16)
    ax.set_ylim(0, max(A_porteuse, A_BL)*1.6)
    ax.legend(loc='upper left', fontsize=10)
    ax.grid(True, alpha=0.3)

    # Répartition de puissance
    P_porteuse = A_porteuse**2 / 2
    P_BL_total = 2 * (A_BL**2 / 2)
    P_totale = P_porteuse + P_BL_total

    textstr = f'Modulation AM (m={m}):\n' + \
              f'• Porteuse présente: {P_porteuse/P_totale*100:.1f}% puissance\n' + \
              f'• Bandes latérales: {P_BL_total/P_totale*100:.1f}% puissance\n' + \
              f'• Démodulation par détection d\'enveloppe possible'
    props = dict(boxstyle='round', facecolor='wheat', alpha=0.5)
    ax.text(0.02, 0.97, textstr, transform=ax.transAxes, fontsize=9,
            verticalalignment='top', bbox=props)

    plt.tight_layout()
    if save:
        plt.savefig(f'spectre_AM_m{m}.png', dpi=300, bbox_inches='tight')
        print(f"Figure sauvegardée: spectre_AM_m{m}.png")
    plt.show()


def comparer_spectres_AM(f0=12000, fs=1500, indices=[0.5, 1.0, 2.0], save=False):
    """
    Compare les spectres AM pour différents indices de modulation
    """
    fig, axes = plt.subplots(1, 3, figsize=(18, 5))

    for idx, m in enumerate(indices):
        ax = axes[idx]

        B0 = 1.0
        A_porteuse = B0
        A_BL = (m * B0) / 2

        # Fréquences
        f_porteuse = f0/1000
        f_BLI = (f0 - fs)/1000
        f_BLS = (f0 + fs)/1000

        # Tracer les raies
        ax.stem([f_porteuse], [A_porteuse], linefmt='g-', markerfmt='go',
                basefmt='k-')
        ax.stem([f_BLI], [A_BL], linefmt='b-', markerfmt='bo', basefmt='k-')
        ax.stem([f_BLS], [A_BL], linefmt='r-', markerfmt='ro', basefmt='k-')

        # Titre et labels
        if m <= 1.0:
            status = "(Correct)"
            color = 'green'
        else:
            status = "(Surmodulation!)"
            color = 'red'

        ax.set_title(f'm = {m} {status}', fontsize=12, fontweight='bold', color=color)
        ax.set_xlabel('Fréquence (kHz)', fontsize=10)
        if idx == 0:
            ax.set_ylabel('Amplitude', fontsize=10)
        ax.set_xlim(8, 16)
        ax.set_ylim(0, max(A_porteuse, A_BL)*1.4)
        ax.grid(True, alpha=0.3)

        # Annotations
        ax.text(f_porteuse, A_porteuse*1.1, f'{A_porteuse:.2f}',
                ha='center', fontsize=9, fontweight='bold')
        ax.text(f_BLI, A_BL*1.1, f'{A_BL:.2f}', ha='center', fontsize=8)
        ax.text(f_BLS, A_BL*1.1, f'{A_BL:.2f}', ha='center', fontsize=8)

    fig.suptitle('Comparaison des spectres AM pour différents indices de modulation\n' +
                 f'f₀ = {f0/1000} kHz, fs = {fs/1000} kHz',
                 fontsize=14, fontweight='bold', y=1.02)

    plt.tight_layout()
    if save:
        plt.savefig('comparaison_spectres_AM.png', dpi=300, bbox_inches='tight')
        print("Figure sauvegardée: comparaison_spectres_AM.png")
    plt.show()


def tracer_signal_temporel_AM(f0=12000, fs=1500, m=0.5, duree=0.005, save=False):
    """
    Trace l'allure temporelle du signal modulé en AM

    M2(t) = B0[1 + m*cos(2πfs*t)]*cos(2πf0*t)
    """
    t = np.linspace(0, duree, 10000)
    B0 = 5.0  # Amplitude de la porteuse (en volts)

    # Signal modulant
    S_t = np.cos(2 * np.pi * fs * t)

    # Signal modulé AM
    M2_t = B0 * (1 + m * S_t) * np.cos(2 * np.pi * f0 * t)

    # Enveloppe
    enveloppe_sup = B0 * (1 + m * S_t)
    enveloppe_inf = -B0 * (1 + m * S_t)

    # Création de la figure
    fig, ax = plt.subplots(figsize=(14, 6))

    # Tracer le signal modulé
    ax.plot(t*1000, M2_t, 'b-', linewidth=0.8, label='Signal modulé M₂(t)')

    # Tracer les enveloppes
    ax.plot(t*1000, enveloppe_sup, 'r--', linewidth=2, label='Enveloppe')
    ax.plot(t*1000, enveloppe_inf, 'r--', linewidth=2)

    # Remplir la zone entre les enveloppes
    ax.fill_between(t*1000, enveloppe_inf, enveloppe_sup, alpha=0.1, color='yellow')

    # Configuration
    ax.set_xlabel('Temps (ms)', fontsize=12, fontweight='bold')
    ax.set_ylabel('Amplitude (V)', fontsize=12, fontweight='bold')
    ax.set_title(f'Signal Modulé en AM - Allure temporelle\n' +
                 f'f₀ = {f0/1000} kHz, fs = {fs/1000} kHz, m = {m}',
                 fontsize=14, fontweight='bold', pad=15)
    ax.grid(True, alpha=0.3)
    ax.legend(loc='upper right', fontsize=10)

    # Informations sur les amplitudes
    A_max = B0 * (1 + m)
    A_min = B0 * (1 - m)

    textstr = f'Indice de modulation: m = {m}\n' + \
              f'Amplitude porteuse: B₀ = {B0} V\n' + \
              f'Amplitude max: {A_max:.2f} V\n' + \
              f'Amplitude min: {A_min:.2f} V\n' + \
              f'Rapport: Amax/Amin = {A_max/A_min if A_min != 0 else "∞":.2f}'

    props = dict(boxstyle='round', facecolor='wheat', alpha=0.7)
    ax.text(0.02, 0.97, textstr, transform=ax.transAxes, fontsize=9,
            verticalalignment='top', bbox=props, family='monospace')

    plt.tight_layout()
    if save:
        plt.savefig(f'signal_temporel_AM_m{m}.png', dpi=300, bbox_inches='tight')
        print(f"Figure sauvegardée: signal_temporel_AM_m{m}.png")
    plt.show()


def comparer_signaux_temporels_AM(f0=12000, fs=1500, indices=[0.5, 1.0, 2.0],
                                   duree=0.005, save=False):
    """
    Compare les signaux temporels AM pour différents indices de modulation
    """
    fig, axes = plt.subplots(3, 1, figsize=(14, 10))

    t = np.linspace(0, duree, 10000)
    B0 = 5.0

    for idx, m in enumerate(indices):
        ax = axes[idx]

        # Signal modulant
        S_t = np.cos(2 * np.pi * fs * t)

        # Signal modulé
        M2_t = B0 * (1 + m * S_t) * np.cos(2 * np.pi * f0 * t)

        # Enveloppes
        enveloppe_sup = B0 * (1 + m * S_t)
        enveloppe_inf = -B0 * (1 + m * S_t)

        # Pour m > 1, gérer le renversement de phase
        if m > 1:
            # Zones où l'enveloppe devient négative
            mask_negative = (1 + m * S_t) < 0
            M2_t_corrected = M2_t.copy()
            M2_t_corrected[mask_negative] = -M2_t_corrected[mask_negative]

            ax.plot(t*1000, M2_t_corrected, 'b-', linewidth=0.8,
                   label='Signal modulé (avec renversement de phase)')

            # Enveloppe redressée
            enveloppe_redressed = np.abs(B0 * (1 + m * S_t))
            ax.plot(t*1000, enveloppe_redressed, 'r--', linewidth=2,
                   label='Enveloppe détectée (distordue)')
            ax.plot(t*1000, -enveloppe_redressed, 'r--', linewidth=2)
        else:
            ax.plot(t*1000, M2_t, 'b-', linewidth=0.8, label='Signal modulé M₂(t)')
            ax.plot(t*1000, enveloppe_sup, 'r--', linewidth=2, label='Enveloppe')
            ax.plot(t*1000, enveloppe_inf, 'r--', linewidth=2)

        ax.axhline(0, color='k', linewidth=0.5, linestyle='-')
        ax.fill_between(t*1000, enveloppe_inf, enveloppe_sup, alpha=0.1, color='yellow')

        # Configuration
        if m <= 1.0:
            title_color = 'green'
            status = "✓ Détection d'enveloppe possible"
        else:
            title_color = 'red'
            status = "✗ Surmodulation - Distorsion"

        ax.set_title(f'm = {m} - {status}', fontsize=12, fontweight='bold',
                    color=title_color)
        ax.set_ylabel('Amplitude (V)', fontsize=10)
        ax.grid(True, alpha=0.3)
        ax.legend(loc='upper right', fontsize=9)

        if idx == 2:
            ax.set_xlabel('Temps (ms)', fontsize=11, fontweight='bold')

    fig.suptitle('Comparaison des signaux temporels AM\n' +
                 f'f₀ = {f0/1000} kHz, fs = {fs/1000} kHz',
                 fontsize=14, fontweight='bold', y=0.995)

    plt.tight_layout()
    if save:
        plt.savefig('comparaison_signaux_AM.png', dpi=300, bbox_inches='tight')
        print("Figure sauvegardée: comparaison_signaux_AM.png")
    plt.show()


def menu_interactif():
    """
    Menu interactif pour choisir le type de graphique à afficher
    """
    print("\n" + "="*60)
    print("  VISUALISATION DES SPECTRES DE MODULATION D'AMPLITUDE")
    print("  TP Modulation - M1 SYSCOM")
    print("="*60)
    print("\nChoisissez le type de graphique à afficher:\n")
    print("1. Spectre DSB (Double Side Band)")
    print("2. Spectre AM (m = 0.5)")
    print("3. Spectre AM (m = 1.0)")
    print("4. Spectre AM (m = 2.0)")
    print("5. Comparaison des spectres AM (m = 0.5, 1.0, 2.0)")
    print("6. Signal temporel AM (m = 0.5)")
    print("7. Signal temporel AM (m = 1.0)")
    print("8. Signal temporel AM (m = 2.0)")
    print("9. Comparaison des signaux temporels AM")
    print("10. Tout afficher")
    print("0. Quitter")
    print("\n" + "="*60)

    choix = input("\nVotre choix (0-10): ")

    return choix


def main():
    """
    Fonction principale
    """
    # Paramètres par défaut du TP
    f0 = 12000  # Hz (12 kHz)
    fs = 1500   # Hz (1.5 kHz)

    while True:
        choix = menu_interactif()

        if choix == '1':
            tracer_spectre_DSB(f0, fs, A_amp=1.0, save=True)
        elif choix == '2':
            tracer_spectre_AM(f0, fs, m=0.5, B0=1.0, save=True)
        elif choix == '3':
            tracer_spectre_AM(f0, fs, m=1.0, B0=1.0, save=True)
        elif choix == '4':
            tracer_spectre_AM(f0, fs, m=2.0, B0=1.0, save=True)
        elif choix == '5':
            comparer_spectres_AM(f0, fs, indices=[0.5, 1.0, 2.0], save=True)
        elif choix == '6':
            tracer_signal_temporel_AM(f0, fs, m=0.5, save=True)
        elif choix == '7':
            tracer_signal_temporel_AM(f0, fs, m=1.0, save=True)
        elif choix == '8':
            tracer_signal_temporel_AM(f0, fs, m=2.0, save=True)
        elif choix == '9':
            comparer_signaux_temporels_AM(f0, fs, indices=[0.5, 1.0, 2.0], save=True)
        elif choix == '10':
            print("\n📊 Génération de tous les graphiques...\n")
            tracer_spectre_DSB(f0, fs, A_amp=1.0, save=True)
            tracer_spectre_AM(f0, fs, m=0.5, B0=1.0, save=True)
            tracer_spectre_AM(f0, fs, m=1.0, B0=1.0, save=True)
            comparer_spectres_AM(f0, fs, indices=[0.5, 1.0, 2.0], save=True)
            tracer_signal_temporel_AM(f0, fs, m=0.5, save=True)
            tracer_signal_temporel_AM(f0, fs, m=1.0, save=True)
            comparer_signaux_temporels_AM(f0, fs, indices=[0.5, 1.0, 2.0], save=True)
            print("\n✅ Tous les graphiques ont été générés et sauvegardés!")
        elif choix == '0':
            print("\n👋 Au revoir!\n")
            break
        else:
            print("\n❌ Choix invalide. Veuillez réessayer.")

        if choix != '0' and choix != '10':
            continuer = input("\nAppuyez sur Entrée pour continuer...")


if __name__ == "__main__":
    main()
