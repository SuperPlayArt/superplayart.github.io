#!/bin/bash
if ! [ -e "public_ip.conf" ]; then
        wget "https://superplayart.github.io/public_ip.conf"
fi
if [ ! -e "scmd.conf" ]; then
    echo "Veuillez saisir votre clé API pour utiliser ce fabuleux système :"
    read api_key
    echo "$api_key" >> scmd.conf
fi
source public_ip.conf
source scmd.conf
while getopts ":c:t:s:d:" option; do
    case "$option" in
        c) # Option -c
            show_description=true
            description_arg="$OPTARG"
            ;;

        t) # Option -t
            show_tutoriel=true
            tutoriel_arg="$OPTARG"
            ;;
        d) # Option -d
            desc="$OPTARG"
            ;;
        s) # Option -s
            sys_type="$OPTARG"
            ;;

        \?) # Option non reconnue
            echo "Option non valide: -$OPTARG"
            exit 1
            ;;
    esac
done
shift $((OPTIND - 1))
search_query="$1"
api_url="http://$PUBLIC_IP/api/index.php?"
if [ "$show_description" = true ]; then
    if [ -n "$description_arg" ]; then
        api_url+="search_cmd=$description_arg"
else
        api_url+="search_cmd=ls"
    fi
fi
if [ "$show_tutoriel" = true ]; then
    if [ -n "$tutoriel_arg" ]; then
        api_url+="search_tutorial=$tutoriel_arg"
else
        api_url+="search_tutorial="
    fi
fi
if [ -n "$sys_type" ]; then
    api_url+="&sys_type=$sys_type"
fi
if [ -n "$desc" ]; then
    api_url+="&description=$desc"
fi

api_url+="&cred=$CRED_API"
command_output=$(curl -s "$api_url")
echo "$command_output"
