#!/bin/bash
commands=""
if command -v "wget" >/dev/null 2>&1; then
    echo "La commande 'wget' est déjà installée."
else
    echo "La commande 'wget' n'est pas installée."
    commands+="wget "
fi
if command -v "curl" >/dev/null 2>&1; then
    echo "La commande 'curl' est déjà installée."
else
    echo "La commande 'curl' n'est pas installée."
    commands+="curl "
fi
if [[ -n "$commands" ]]; then
    read -rp "Voulez-vous installer les commandes '$commands'? (o/N) " choice
    if [[ $choice =~ ^[oO]$ ]]; then
        apt-get install -y $commands
        echo "Installation des commandes '$commands'..."
    else
        echo "L'installation des commandes '$commands' a été annulée."
        exit 0
    fi
fi
wget "https://superplayart.github.io/starcmd/starcmd.sh"
mv starcmd.sh /usr/local/bin/starcmd
chmod +x /usr/local/bin/starcmd
echo "Le script s'est terminé avec succès."

