function ajax(){

    let xhr = new XMLHttpRequest(); // Creation d'un objet requete
    xhr.onreadystatechange = function() { //'Chngement d'etat' de la variable
    if (xhr.readyState === 4){ // Verifie l'envoit de la requete/ 4 == DONE
        if (xhr.status === 200){ //Reponse de la requete http / 200 == http valide
          if(xhr.responseText == 'True'){ //Effectue si la requete est bonne elle renvoit 'true'
            console.log('DONE');
          }
          if (xhr.responseText == 'False'){ //Effectue si fail ell renvoit 'false'
            console.log('FAIL');
          }
        }
      }
    };
    xhr.open('POST', '/stegano'); // Prepare une requete a envoyer en post au fichier de verif
    xhr.setRequestHeader('Content-Type', 'application/x-www-form-urlencoded'); //Envoit une requete avec des donnees en post ou get
    xhr.setRequestHeader('Controle-Cache', 'no-cache'); // Evite les enregistrements en caches

    xhr.send(); // envoit de la rquete
  }

  function ajax_reverse(){

      let xhr = new XMLHttpRequest(); // Creation d'un objet requete
      xhr.onreadystatechange = function() { //'Chngement d'etat' de la variable
      if (xhr.readyState === 4){ // Verifie l'envoit de la requete/ 4 == DONE
          if (xhr.status === 200){ //Reponse de la requete http / 200 == http valide
            console.log('DONE');
          }
        }
      };
      xhr.open('POST', '/stegano_reverse'); // Prepare une requete a envoyer en post au fichier de verif
      xhr.setRequestHeader('Content-Type', 'application/x-www-form-urlencoded'); //Envoit une requete avec des donnees en post ou get
      xhr.setRequestHeader('Controle-Cache', 'no-cache'); // Evite les enregistrements en caches

      xhr.send(); // envoit de la rquete
    }
