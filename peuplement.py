from stages.models.candidature import Candidature
from stages.models.competence import Competence
from stages.models.enseignant_referent import Enseignant_referent
from stages.models.entreprise import Entreprise
from stages.models.etudiant import Etudiant
from stages.models.offre import Offre
from stages.models.stage import Stage
from stages.models.tuteur_entreprise import Tuteur_entreprise

python = Competence.objects.create(libelle="Python")
django = Competence.objects.create(libelle="Django")
sql = Competence.objects.create(libelle="Sql")
css = Competence.objects.create(libelle="css")
html = Competence.objects.create(libelle="html")

entreprise1 = Entreprise.objects.create(nom="ecobank", ville="Sokode")
entreprise2 = Entreprise.objects.create(nom="SheConnect", ville="Sokode")
entreprise3 = Entreprise.objects.create(nom="Atd", ville="Lomé")

tuteur1 = Tuteur_entreprise.objects.create(nom="Koffi", prenom="Jean", sexe="Homme", date_naissance="1985-05-12", email="jean.koffi@example.com", entreprise=entreprise1)
tuteur2 = Tuteur_entreprise.objects.create(nom="Mensah", prenom="Afi", sexe="Femme", date_naissance="1988-09-20", email="afi.mensah@example.com", entreprise=entreprise2)

enseignant1 = Enseignant_referent.objects.create(nom="Pierre", prenom="Jean", sexe="Homme", date_naissance="1980-03-15", email="pierre.amouzou@example.com")
enseignant2 = Enseignant_referent.objects.create(nom="Curie", prenom="Marie", sexe="Femme", date_naissance="1983-07-10", email="marie.kouassi@example.com")

etudiant1 = Etudiant.objects.create(nom="Kossi", prenom="Ama", sexe="Femme", date_naissance="2003-02-10", email="kossi@example.com", matricule="ETU001", promotion="2026")
etudiant2 = Etudiant.objects.create(nom="Tchalla", prenom="Komlan", sexe="Homme", date_naissance="2002-06-18", email="komlan@example.com", matricule="ETU002", promotion="2026")
etudiant3 = Etudiant.objects.create(nom="Adjeoda", prenom="Mawuli", sexe="Homme", date_naissance="2003-01-25", email="mawuli@example.com", matricule="ETU003", promotion="2026")
etudiant4 = Etudiant.objects.create(nom="Assih", prenom="Eyram", sexe="Femme", date_naissance="2002-11-05", email="eyram@example.com", matricule="ETU004", promotion="2026")
etudiant5 = Etudiant.objects.create(nom="Douti", prenom="Kodjo", sexe="Homme", date_naissance="2003-08-22", email="kodjo@example.com", matricule="ETU005", promotion="2026")

etudiant1.competences.add(python, django, sql)
etudiant2.competences.add(html, python)
etudiant3.competences.add(python, sql)
etudiant4.competences.add(html)
etudiant5.competences.add(python, django, css)

offre1 = Offre.objects.create(titre="Developpeur web Django", description="Developpement d'une application web avec Django.", date_debut="2026-06-01", date_fin="2026-08-31", nb_places=2, entreprise=entreprise1)
offre2 = Offre.objects.create(titre="Assistant reseau informatique", description="Installation et maintenance des equipements reseau.", date_debut="2026-06-15", date_fin="2026-08-15", nb_places=1, entreprise=entreprise2)
offre3 = Offre.objects.create(titre="Developpeur frontend", description="Creation d'interfaces web modernes.", date_debut="2026-07-01", date_fin="2026-09-30", nb_places=2, entreprise=entreprise3)
offre4 = Offre.objects.create(titre="Developpeur Backend Django", description="Developpement d'API REST et gestion des bases de donnees.", date_debut="2026-11-01", date_fin="2027-04-30", nb_places=1, entreprise=entreprise1)
offre5 = Offre.objects.create(titre="Data Analyst", description="Analyse des donnees utilisateurs et optimisation des requetes SQL.", date_debut="2026-12-15", date_fin="2027-03-15", nb_places=2, entreprise=entreprise2)
offre6 = Offre.objects.create(titre="Developpeur Fullstack", description="Maintenance de l'application interne, de l'interface au serveur.", date_debut="2027-01-01", date_fin="2027-06-30", nb_places=3, entreprise=entreprise3)


offre1.competences.add(python, django, sql)
offre2.competences.add(sql)
offre3.competences.add(html, python)

candidature1 = Candidature.objects.create(etudiant=etudiant1, offre=offre1, date_depot="2026-04-01", statut="Retenue")
candidature2 = Candidature.objects.create(etudiant=etudiant2, offre=offre1, date_depot="2026-04-02", statut="Refuse")
candidature3 = Candidature.objects.create(etudiant=etudiant3, offre=offre2, date_depot="2026-04-03", statut="Retenue")
candidature4 = Candidature.objects.create(etudiant=etudiant4, offre=offre2, date_depot="2026-04-04", statut="Depose")
candidature5 = Candidature.objects.create(etudiant=etudiant5, offre=offre3, date_depot="2026-04-05", statut="Refuse")
candidature6 = Candidature.objects.create(etudiant=etudiant1, offre=offre3, date_depot="2026-04-06", statut="Depose")

Stage.objects.create(sujet="Developpement d'une application Django", candidature=candidature1, tuteur_entreprise=tuteur1, enseignant_referent=enseignant1)
Stage.objects.create(sujet="Mise en place reseau", candidature=candidature3, tuteur_entreprise=tuteur2, enseignant_referent=enseignant2)


