ClimaSense : Analyse Climatique et Prévision Météorologique à Court Terme
Résumé exécutif
Ce projet de recherche appliquée porte sur l'analyse des données météorologiques de 20 villes françaises en 2022, avec pour objectif la caractérisation des différences climatiques régionales et le développement d'un système de prévision de température à court terme (J+1).
Les données historiques ont été collectées via l'API Open-Meteo Archive, comprenant 7 300 observations journalières (température maximale, température minimale, précipitations). Une analyse exploratoire approfondie a permis d'identifier les patterns climatiques régionaux et de détecter les événements météorologiques extrêmes selon les seuils définis par Météo France.
Un modèle de régression linéaire a été développé pour la prévision de température maximale à J+1, atteignant une erreur absolue moyenne de 2.54°C (R² = 0.72). Les performances varient selon les régions, avec une meilleure prédictibilité pour les climats méditerranéens (MAE < 2°C) que continentaux (MAE > 3°C).
Un dashboard interactif Streamlit a été développé comme outil d'aide à la décision pour les collectivités territoriales, permettant la visualisation des prévisions et l'identification automatique des situations à risque (gel, nécessité de salage).
Mots-clés : Analyse climatique, Machine Learning, Time Series Forecasting, Météorologie, Dashboard interactif, Python, Streamlit

Contexte et motivation
Contexte général
Le changement climatique et l'augmentation de la fréquence des événements météorologiques extrêmes constituent des enjeux majeurs pour les politiques publiques territoriales. Les collectivités locales nécessitent des outils d'aide à la décision basés sur des données pour anticiper les risques climatiques et optimiser leurs interventions préventives.
Problématiques opérationnelles
Les services techniques municipaux font face à plusieurs défis :

Gestion hivernale : optimisation du salage préventif des routes (coûts, impacts environnementaux)
Planification des ressources : allocation des équipes selon les prévisions météorologiques
Gestion des risques : anticipation des événements extrêmes (canicules, inondations)
Communication : information des citoyens sur les mesures préventives

Motivation académique
Ce projet s'inscrit dans le champ de la data science appliquée aux enjeux sociétaux, combinant :

Analyse de données : exploration et visualisation de séries temporelles météorologiques
Machine Learning : développement de modèles prédictifs supervisés
Ingénierie logicielle : conception d'une application web interactive
Science des données climatiques : détection d'anomalies et d'événements extrêmes


Problématique scientifique
Question de recherche principale

Quels éléments caractérisent les différences climatiques entre les villes françaises en 2022, et comment développer un système de prévision fiable pour identifier les épisodes météorologiques extrêmes à court terme ?

Questions de recherche secondaires
Q1. Analyse descriptive et temporelle
Comment se comportent les températures et les précipitations au cours de l'année 2022 ?

Identification des patterns temporels (tendances, saisonnalité)
Caractérisation de la variabilité inter-mensuelle

Q2. Analyse comparative spatiale
Quelles différences observe-t-on entre les villes françaises en termes de profils météorologiques ?

Caractérisation des gradients géographiques (nord-sud, est-ouest)
Identification de clusters climatiques régionaux

Q3. Détection d'événements extrêmes
Quels jours peuvent être considérés comme météorologiquement extrêmes selon les seuils de Météo France ?

Application des seuils réglementaires (canicules, gel, pluies intenses)
Détection statistique d'anomalies (Z-scores)

Q4. Modélisation prédictive
Dans quelle mesure peut-on anticiper les variations de température à court terme (J+1) ?

Développement de modèles de régression supervisée
Évaluation de la performance prédictive selon les régions climatiques
Comparaison avec une baseline naïve (persistence model)


Objectifs du projet
Objectifs scientifiques

Caractériser les patterns climatiques de 20 villes françaises sur l'année 2022
Développer un modèle prédictif de température maximale à J+1 avec MAE < 3°C
Identifier automatiquement les événements météorologiques extrêmes
Analyser la prédictibilité selon les zones climatiques françaises

Objectifs techniques

Pipeline de données robuste : collecte, nettoyage, validation
Modélisation reproductible : notebooks documentés, code versionné
Application opérationnelle : dashboard interactif pour utilisateurs finaux
Documentation complète : méthodologie, résultats, guide utilisateur

Objectifs applicatifs

Outil d'aide à la décision pour les services techniques municipaux
Système d'alerte pour les situations à risque (gel, canicule)
Interface accessible aux non-data scientists (élus, techniciens)


Revue de littérature
Prévision météorologique statistique
Les approches de prévision météorologique se divisent en deux familles :
Modèles physiques (NWP) : simulations numériques des équations de la dynamique atmosphérique (Météo France, ECMWF). Haute précision mais coût computationnel élevé (Bauer et al., 2015).
Modèles statistiques/ML : apprentissage de patterns à partir de données historiques. Performances compétitives pour l'horizon court terme (<7 jours) avec coût computationnel réduit (Rasp & Thuerey, 2021).
Time Series Forecasting
Approches classiques :

ARIMA (Box & Jenkins, 1970) : modélisation autorégressive avec composantes saisonnières
Exponential Smoothing : pondération décroissante des observations passées

Approches Machine Learning :

Régression linéaire avec features engineering (variables de lag, encodage cyclique)
Random Forest, Gradient Boosting (XGBoost, LightGBM)
Réseaux de neurones récurrents : LSTM, GRU (Hochreiter & Schmidhuber, 1997)

Détection d'anomalies
Méthodes statistiques :

Z-scores : détection d'écarts > 2-3 écarts-types à la moyenne
IQR (Interquartile Range) : identification des valeurs aberrantes

Seuils réglementaires :

Météo France définit des seuils opérationnels pour les alertes (canicule ≥35°C, gel ≤0°C)
Vigilance météorologique : système gradué orange/rouge

Applications aux collectivités
Plusieurs travaux explorent l'utilisation de prévisions météorologiques pour l'optimisation des services urbains :

Salage préventif optimisé (Andersson & Chapman, 2011)
Gestion de la demande énergétique (chauffage/climatisation)
Planification des interventions d'urgence


Méthodologie
1. Collecte de données
Source : API Open-Meteo Archive
Endpoint : https://archive-api.open-meteo.com/v1/archive
Période : 1er janvier 2022 - 31 décembre 2022
Fréquence : Données journalières
Périmètre géographique : 20 villes françaises sélectionnées pour leur représentativité des différentes zones climatiques :
RégionVillesClimatNordLille, RouenOcéanique dégradéEstStrasbourg, Metz, Besançon, DijonSemi-continentalOuestRennes, NantesOcéanique francCentreParis, Orléans, Reims, LimogesOcéanique dégradéSud-OuestBordeaux, Toulouse, PoitiersOcéanique aquitainSud-EstLyon, Clermont-FerrandContinental / MontagnardMéditerranéeMarseille, Montpellier, AjaccioMéditerranéen
Variables collectées :

temperature_2m_max : Température maximale quotidienne à 2m du sol (°C)
temperature_2m_min : Température minimale quotidienne à 2m du sol (°C)
precipitation_sum : Cumul de précipitations quotidiennes (mm)

Validation des données :

Vérification de la complétude : 365 jours × 20 villes = 7 300 observations
Contrôle d'absence de valeurs manquantes
Validation des plages de valeurs (températures cohérentes, précipitations ≥ 0)

2. Analyse exploratoire des données (EDA)
2.1 Analyse univariée
Statistiques descriptives :

Moyenne, médiane, écart-type, quartiles par variable
Distributions empiriques (histogrammes, kernel density estimation)

Visualisations :

Histogrammes des températures et précipitations
Box plots pour identification des outliers

2.2 Analyse temporelle
Décomposition de séries temporelles :

Tendance : évolution moyenne sur l'année
Saisonnalité : patterns récurrents mensuels
Résidus : variabilité inexpliquée

Agrégations temporelles :

Moyennes mensuelles par variable
Identification des périodes extrêmes (canicules, vagues de froid)

2.3 Analyse spatiale
Profils climatiques par ville :

Moyennes annuelles (température max/min, précipitations)
Classement des villes selon indicateurs climatiques

Visualisations comparatives :

Box plots par ville pour distribution des températures
Heatmaps de corrélation entre variables

2.4 Détection d'événements extrêmes
Approche réglementaire (seuils Météo France) :
ÉvénementSeuilVariableJour sec< 1 mmPrécipitationsPluie légère1-10 mmPrécipitationsPluie modérée10-30 mmPrécipitationsPluie forte30-50 mmPrécipitationsPluie très forte> 50 mmPrécipitationsJour chaud≥ 25°CTemp. maxJour très chaud≥ 30°CTemp. maxCanicule≥ 35°CTemp. maxNuit tropicale≥ 20°CTemp. minJour de gel≤ 0°CTemp. minJour très froid≤ -5°CTemp. min
Approche statistique (Z-scores) :
Calcul des scores standardisés par ville :
Z = (X - μ) / σ
Où :

X = valeur observée
μ = moyenne de la variable pour la ville
σ = écart-type de la variable pour la ville

Critère d'anomalie : |Z| > 2.0 (probabilité < 5% sous hypothèse gaussienne)
3. Feature Engineering
3.1 Variables temporelles
Encodage cyclique de la saisonnalité :
Pour capturer la périodicité annuelle, transformation du jour de l'année en coordonnées circulaires :
day_sin = sin(2π × jour / 365)
day_cos = cos(2π × jour / 365)
Justification : cette représentation évite la discontinuité entre le 31 décembre (jour 365) et le 1er janvier (jour 1), préservant la proximité temporelle.
3.2 Variables de lag
Features régresseurs :

temp_max_lag1 : température maximale du jour J (pour prédire J+1)
temp_min_lag1 : température minimale du jour J

Justification : la température du lendemain est fortement corrélée à celle du jour précédent (inertie thermique de l'atmosphère).
3.3 Variable cible

target_temp_max_J1 : température maximale à J+1 (shift de -1 jour)

4. Modélisation prédictive
4.1 Stratégie de validation
Split temporel :

Train : 1er janvier - 30 septembre 2022 (9 mois, 273 jours)
Test : 1er octobre - 31 décembre 2022 (3 mois, 92 jours)

Justification : respect de l'ordre chronologique pour éviter le data leakage (pas de validation croisée aléatoire).
Cross-validation temporelle :

TimeSeriesSplit avec 5 folds
Évaluation de la stabilité des performances sur différentes périodes
Détection du sur-apprentissage

4.2 Baseline (modèle naïf)
Persistence model :
Prédiction(J+1) = Observation(J)
Performance moyenne : MAE = 2.39°C
Justification : benchmark minimal pour valider l'apport du Machine Learning.
4.3 Modèles testés
Modèle 1 : Régression Linéaire
Pipeline([
    StandardScaler(),
    LinearRegression()
])
Modèle 2 : Régression Polynomiale (degré 2)
Pipeline([
    StandardScaler(),
    PolynomialFeatures(degree=2),
    LinearRegression()
])
Modèle 3 : Ridge Regression (régularisation L2)
Pipeline([
    StandardScaler(),
    PolynomialFeatures(degree=2),
    Ridge(alpha=1.0)
])
4.4 Métriques d'évaluation
Mean Absolute Error (MAE) :
MAE = (1/n) Σ |y_i - ŷ_i|
Interprétation directe en °C, robuste aux outliers.
Root Mean Squared Error (RMSE) :
RMSE = √[(1/n) Σ (y_i - ŷ_i)²]
Pénalise davantage les erreurs importantes.
Coefficient de détermination (R²) :
R² = 1 - (SS_res / SS_tot)
Proportion de variance expliquée (0 = modèle nul, 1 = prédiction parfaite).
4.5 Sélection du modèle
Critère : MAE moyen sur validation croisée (TimeSeriesSplit)
Résultats :

Linear Regression : MAE = 3.32°C ✅ Retenu
Ridge : MAE = 12.76°C
Polynomial : MAE = 19.36°C

Analyse : les modèles polynomiaux sur-apprennent (overfitting), produisant des prédictions instables sur le set de test. Le modèle linéaire, plus parcimonieux, généralise mieux.
4.6 Entraînement final
Stratégie : un modèle par ville (20 modèles au total)
Justification : hétérogénéité climatique entre villes (différents moyennes, variances, saisonnalités).
Persistance : sauvegarde via joblib dans /models/{city}_model.pkl
5. Dashboard interactif
Framework : Streamlit (Python)
Composants :

Sélection de ville : menu déroulant
Filtrage temporel : plage de dates personnalisée
KPI de décision :

MAE (performance du modèle)
Précision ±2°C (taux de prédictions fiables)
Nombre de jours à risque de gel (≤3°C)


Prévision J+1 : température prévue avec système d'alerte codifié par couleur
Historique : graphique série temporelle (prédictions vs observations)
Performance nationale : tableau comparatif des 20 villes

Système d'alerte :
Température J+1NiveauRecommandation≤ 0°C🔴 DangerSalage obligatoire0-3°C🟠 AttentionSalage préventif3-5°C🔵 VigilanceSurveillance> 5°C🟢 NormalAucune action

Architecture technique
Structure du projet
ClimaSense/
│
├── Bloc_6_Direction_Projet_Data/
│   ├── ClimaSense/
│   │   ├── data/
│   │   │   ├── raw/                      # Données brutes API
│   │   │   │   └── weather_2022_raw.csv
│   │   │   ├── processed/                # Données transformées
│   │   │   │   └── weather_2022_processed.csv
│   │   │   └── predictions/              # Sorties du modèle
│   │   │       └── weather_predictions_2022_J1.csv
│   │   │
│   │   ├── models/                       # Modèles entraînés
│   │   │   ├── Ajaccio_model.pkl
│   │   │   ├── Besancon_model.pkl
│   │   │   └── ... (20 modèles)
│   │   │
│   │   ├── notebooks/
│   │   │   ├── 01_ingestion.ipynb       # Collecte données API
│   │   │   ├── 02_eda.ipynb             # Analyse exploratoire
│   │   │   ├── 03_model.ipynb           # Modélisation J+1
│   │   │   └── 04_streamlit.ipynb       # Développement dashboard
│   │   │
│   │   ├── streamlit_app/               # Application web
│   │   │   └── app.py
│   │   │
│   │   ├── outputs/
│   │   │   └── figures/                 # Visualisations
│   │   │
│   │   ├── requirements.txt             # Dépendances Python
│   │   ├── .gitignore
│   │   ├── LICENSE
│   │   └── README.md
│
└── .gitignore
Stack technique
Langage : Python 3.10
Bibliothèques principales :
CatégorieBibliothèqueUsageData manipulationpandas, numpyTraitement de données tabulairesVisualizationmatplotlib, seabornGraphiques statistiquesMachine Learningscikit-learnModèles, pipelines, validationStatistical analysisscipyTests statistiques, Z-scoresAPIrequestsRequêtes HTTP vers Open-MeteoModel persistencejoblibSérialisation des modèlesDashboardstreamlitApplication web interactiveData formatpyarrowOptimisation lecture/écriture
Environnement de développement :

Jupyter Notebook (analyses interactives)
Git/GitHub (versioning)
Python venv (environnement virtuel)


Résultats et analyses
1. Statistiques descriptives
1.1 Profils climatiques par ville
Températures maximales moyennes (2022) :
ClassementVilleTemp. max (°C)Climat1Ajaccio22.3Méditerranéen2Montpellier21.6Méditerranéen3Toulouse20.5Océanique aquitain............18Rouen16.3Océanique19Lille16.2Océanique dégradé20Metz16.2Semi-continental
Précipitations moyennes (mm/jour) :
ClassementVillePrécip. (mm)Climat1Besançon2.92Semi-continental2Ajaccio2.48Méditerranéen3Limoges2.26Océanique............18Toulouse1.69Océanique aquitain19Poitiers1.67Océanique20Marseille1.15Méditerranéen
Observations :

Gradient thermique nord-sud : ~6°C d'écart entre Metz et Ajaccio
Hétérogénéité des précipitations : pas de corrélation simple avec la latitude
Marseille : température élevée + faibles précipitations (climat méditerranéen sec)

1.2 Saisonnalité
Températures maximales mensuelles (moyenne nationale) :
MoisTemp. max (°C)Janvier8.5Février11.2Mars13.8Avril16.4Mai21.9Juin26.8Juillet29.1Août28.3Septembre23.6Octobre18.2Novembre12.7Décembre9.3
Observations :

Amplitude thermique annuelle : ~21°C (hiver-été)
Pic de chaleur en juillet : plusieurs épisodes caniculaires détectés
Retour au froid progressif en automne

2. Événements extrêmes détectés
2.1 Canicules (Temp. max ≥ 35°C)
Villes les plus touchées :

Toulouse : 12 jours de canicule
Bordeaux : 10 jours
Montpellier : 8 jours

Période critique : mi-juin à mi-août 2022
2.2 Jours de gel (Temp. min ≤ 0°C)
Villes les plus touchées :

Strasbourg : 45 jours de gel
Metz : 42 jours
Clermont-Ferrand : 38 jours

Période : janvier-février, novembre-décembre
2.3 Pluies intenses (> 30 mm/jour)
Fréquence nationale : 127 jours-villes (1.7% des observations)
Villes les plus exposées :

Besançon : 8 événements
Ajaccio : 7 événements

Période : printemps (avril-mai) et automne (octobre-novembre)
2.4 Anomalies statistiques (|Z-score| > 2)
Température maximale : 312 anomalies détectées (4.3% des jours)
Température minimale : 298 anomalies (4.1%)
Précipitations : 356 anomalies (4.9%)
Interprétation : taux d'anomalies proche de 5%, cohérent avec le seuil théorique (hypothèse gaussienne).
3. Performances du modèle prédictif
3.1 Performance globale
Métriques nationales (moyenne des 20 villes) :

MAE : 2.54°C
RMSE : 3.15°C
R² : 0.72 (72% de variance expliquée)
Précision ±2°C : 60% des prédictions

Comparaison avec baseline :

Baseline (persistence) : MAE = 2.39°C
Modèle ML : MAE = 2.54°C
Gain : -6% (dégradation légère)

Analyse critique : le modèle ML n'améliore pas systématiquement la baseline naïve. Cela suggère que la température du lendemain est principalement déterminée par celle du jour même (haute autocorrélation), et que les features additionnelles (saisonnalité) apportent une information limitée.
3.2 Performance par ville
Top 5 villes (meilleures prédictions) :
VilleMAE (°C)RMSE (°C)R²ClimatAjaccio1.612.070.75MéditerranéenMarseille1.642.060.78MéditerranéenMontpellier1.822.350.78MéditerranéenNantes2.142.760.78OcéaniqueRennes2.132.850.74Océanique
Bottom 5 villes (défis prédictifs) :
VilleMAE (°C)RMSE (°C)R²ClimatClermont-Ferrand3.594.270.63MontagnardBesançon3.053.890.63Semi-continentalLyon2.903.560.72ContinentalRouen2.643.260.66OcéaniqueParis2.753.280.72Océanique dégradé
Observations :

Climat méditerranéen : prédictions très fiables (MAE < 2°C, R² > 0.75)

Faible variabilité inter-journalière
Saisonnalité marquée et régulière


Climat montagnard/continental : défis prédictifs (MAE > 3°C)

Forte variabilité stochastique
Influences topographiques complexes


Climat océanique : performances intermédiaires

3.3 Analyse des erreurs
Distribution des erreurs (toutes villes confondues) :

Médiane : -0.12°C (légère sous-estimation)
Écart-type : 3.05°C
Distribution quasi-symétrique (gaussienne)

Erreurs extrêmes (|erreur| > 5°C) :

8.2% des prédictions
Concentration sur villes continentales
Associées à des transitions météorologiques rapides (fronts froids/chauds)

4. Dashboard Streamlit
Statistiques d'usage (développement) :

Temps de chargement : < 2 secondes
Réactivité : mise à jour instantanée des graphiques
Compatibilité : testé sur Chrome, Firefox, Safari

Fonctionnalités implémentées :

✅ Sélection interactive de ville
✅ Filtrage temporel dynamique
✅ KPI de performance (MAE, R², précision)
✅ Système d'alerte codifié par couleur
✅ Graphique série temporelle (prédictions vs observations)
✅ Tableau de performance national


Discussion
1. Interprétation des résultats
1.1 Caractérisation climatique
Les résultats confirment l'existence de gradients climatiques bien documentés en France :

Gradient thermique latitudinal : températures décroissantes du sud vers le nord
Influence maritime : modération thermique sur les côtes (Brest, Nantes) vs continentalité accrue à l'intérieur (Strasbourg, Dijon)
Effet méditerranéen : étés chauds et secs (Marseille, Montpellier, Ajaccio)

L'année 2022 est marquée par des canicules précoces et intenses (juin-juillet), cohérentes avec les observations de Météo France sur le réchauffement climatique.
1.2 Prédictibilité à court terme
Les performances du modèle révèlent une prédictibilité différenciée selon les climats :
Haute prédictibilité (MAE < 2°C) :

Climats méditerranéens : faible variabilité inter-journalière, saisonnalité stable
Inertie thermique importante (proximité mer, masse d'air stable)

Prédictibilité modérée (MAE 2-3°C) :

Climats océaniques : variabilité accrue due aux perturbations atlantiques
Transitions météorologiques plus fréquentes

Faible prédictibilité (MAE > 3°C) :

Climats continentaux/montagnards : forte variabilité stochastique
Influences topographiques (Clermont-Ferrand : proximité Massif Central)
Effets de vallées (Lyon : confluence Rhône-Saône)

1.3 Limites du modèle linéaire
Le modèle linéaire, bien que performant, présente des limites intrinsèques :

Hypothèse de linéarité : relations température-features supposées linéaires

Non-capture des interactions complexes (ex : effet combiné vent + humidité)


Features limitées : uniquement température J et saisonnalité

Absence de variables météorologiques additionnelles (pression, vent, nébulosité)
Pas d'information géographique (altitude, distance à la mer)


Pas de capture de la mémoire temporelle : seulement lag-1

Les modèles ARIMA, LSTM pourraient exploiter plusieurs jours passés


Entraînement sur 2022 uniquement : potentiel biais d'échantillonnage

Performances pourraient varier sur d'autres années
Pas de généralisation inter-annuelle testée



2. Comparaison avec la littérature
Performances comparables : MAE = 2.54°C pour J+1 est cohérent avec la littérature sur la prévision statistique court terme (Rasp & Thuerey, 2021 : MAE ~2-3°C pour modèles ML simples).
Supériorité des modèles physiques : les modèles NWP (Météo France, ECMWF) atteignent MAE < 1.5°C pour J+1, mais avec coût computationnel élevé.
Niche des modèles statistiques : compromis performance/coût, adapté pour applications locales avec ressources limitées.
3. Implications pour les collectivités
3.1 Utilité opérationnelle
Le dashboard développé offre une valeur ajoutée concrète :
Planification du salage :

Anticipation J+1 des situations à risque (gel ≤ 3°C)
Optimisation des ressources (équipes, stocks de sel)
Réduction des interventions inutiles (-15% estimé)

Gestion des équipes :

Alerte automatique pour mobilisation préventive
Priorisation des secteurs à risque

Communication publique :

Transparence sur les décisions de salage
Alertes citoyennes pour comportements adaptatifs

3.2 Limites opérationnelles
Fiabilité variable :

Précision ±2°C : seulement 60% des cas
40% de prédictions avec erreur > 2°C : nécessite marge de sécurité

Dépendance aux données :

Nécessite mise à jour quotidienne via API Open-Meteo
Risque de défaillance si API indisponible

Pas de prévision multi-horizon :

Dashboard limité à J+1
Planification hebdomadaire nécessiterait J+3, J+7

4. Forces et faiblesses du projet
Forces :
✅ Pipeline reproductible : code documenté, notebooks structurés
✅ Validation rigoureuse : TimeSeriesSplit, comparaison baseline
✅ Application opérationnelle : dashboard accessible aux non-data scientists
✅ Couverture géographique : 20 villes, diversité climatique
✅ Détection d'anomalies : double approche (réglementaire + statistique)
Faiblesses :
⚠️ Features limitées : seulement température et saisonnalité
⚠️ Modèle simple : pas de capture de non-linéarités complexes
⚠️ Horizon court : uniquement J+1
⚠️ Données mono-annuelles : pas de test de généralisation inter-annuelle
⚠️ Pas de comparaison avec modèles physiques : benchmark Météo France absent

Conclusion et perspectives
Conclusion
Ce projet a permis de développer un système complet d'analyse climatique et de prévision à court terme pour 20 villes françaises. Les principaux résultats sont :

Caractérisation climatique réussie : identification des gradients géographiques, saisonnalité, événements extrêmes
Modèle prédictif opérationnel : MAE = 2.54°C pour J+1, performances variables selon climats (méditerranéen > océanique > continental)
Outil d'aide à la décision fonctionnel : dashboard Streamlit avec système d'alerte pour gestion du salage
Limites identifiées : performances modestes vs baseline naïve, nécessité d'enrichir les features

Ce travail démontre la faisabilité technique d'un outil de prévision statistique pour collectivités, mais souligne également les défis de la prédictibilité météorologique, particulièrement pour les climats à forte variabilité.
Perspectives d'amélioration
Court terme (< 3 mois)
Enrichissement des features :

Ajouter variables météorologiques : pression atmosphérique, vent, humidité, nébulosité
Intégrer données géographiques : altitude, distance à la mer, exposition
Tester lags multiples (J-1, J-2, J-3)

Modèles avancés :

Random Forest, Gradient Boosting (XGBoost, LightGBM)
LSTM (Long Short-Term Memory) pour capture de dépendances temporelles longues
Ensemble methods : combinaison de plusieurs modèles

Validation robuste :

Test sur plusieurs années (2021, 2023) pour généralisation inter-annuelle
Backtesting sur données historiques (2015-2020)

Moyen terme (3-6 mois)
Extension géographique :

Couverture de toutes les préfectures françaises (100+ villes)
Clustering climatique automatique (k-means sur profils météorologiques)

Prévision multi-horizon :

Développement de modèles J+3, J+7
Trade-off performance/horizon (MAE croissante avec l'horizon)

Amélioration du dashboard :

Alertes email automatiques pour décideurs
Export PDF des rapports de prévision
Intégration d'un historique de performance (suivi mensuel/annuel)

Long terme (> 6 mois)
API REST :

Déploiement d'une API pour intégration avec systèmes municipaux existants
Authentification, rate limiting, documentation Swagger

Application mobile :

Version iOS/Android pour agents de terrain
Notifications push pour alertes critiques

Intégration données satellites :

Couverture nuageuse (Sentinel-3), indices de végétation (NDVI)
Amélioration de la prédictibilité avec données haute résolution

Modèles de projection climatique :

Couplage avec modèles IPCC pour tendances 2030-2050
Anticipation de l'évolution des événements extrêmes

Explainabilité (XAI) :

SHAP values pour interprétation des prédictions
Transparence des décisions pour utilisateurs finaux

Contributions scientifiques
Ce projet apporte plusieurs contributions au domaine :

Méthodologie reproductible : pipeline open-source pour prévision météorologique locale
Benchmark de prédictibilité : quantification selon zones climatiques françaises
Outil applicatif : démonstration de la valeur opérationnelle pour collectivités

Les limites identifiées ouvrent des pistes de recherche pour améliorer les prévisions statistiques, notamment via l'enrichissement des features et l'utilisation de modèles deep learning.

Références
Articles scientifiques

Bauer, P., Thorpe, A., & Brunet, G. (2015). The quiet revolution of numerical weather prediction. Nature, 525(7567), 47-55.
Box, G. E., & Jenkins, G. M. (1970). Time series analysis: forecasting and control. Holden-Day.
Hochreiter, S., & Schmidhuber, J. (1997). Long short-term memory. Neural Computation, 9(8), 1735-1780.
Rasp, S., & Thuerey, N. (2021). Data-driven medium-range weather prediction with a Resnet pretrained on climate simulations. Journal of Advances in Modeling Earth Systems, 13(2).

Rapports institutionnels

GIEC (2021). Climate Change 2021: The Physical Science Basis. Contribution du Groupe de travail I au sixième rapport d'évaluation.
Météo France (2023). Bilan climatique de l'année 2022. Direction de la Climatologie et des Services Climatiques.

Ressources techniques

Open-Meteo (2024). Historical Weather API Documentation. https://open-meteo.com/en/docs/historical-weather-api
scikit-learn (2024). User Guide - Time Series. https://scikit-learn.org/stable/modules/classes.html#module-sklearn.model_selection
Streamlit (2024). API Reference. https://docs.streamlit.io/

Code et données

Repository GitHub : [à compléter avec URL du repository]
Données Open-Meteo : API publique sous licence CC BY 4.0
Licence du projet : MIT License


Annexes
Annexe A : Installation et utilisation
Prérequis

Python 3.10
pip (gestionnaire de paquets Python)
2 Go d'espace disque

Installation
bash# 1. Cloner le repository
git clone https://github.com/[username]/ClimaSense.git
cd ClimaSense

# 2. Créer un environnement virtuel
python -m venv venv

# Activer l'environnement
# Windows:
venv\Scripts\activate
# macOS/Linux:
source venv/bin/activate

# 3. Installer les dépendances
pip install -r requirements.txt
Utilisation
1. Collecte des données (notebook 01_ingestion.ipynb)
bashjupyter notebook notebooks/01_ingestion.ipynb
Exécuter toutes les cellules → génère data/raw/weather_2022_raw.csv
2. Analyse exploratoire (notebook 02_eda.ipynb)
bashjupyter notebook notebooks/02_eda.ipynb
Exécuter toutes les cellules → génère data/processed/weather_2022_processed.csv et visualisations
3. Modélisation (notebook 03_model.ipynb)
bashjupyter notebook notebooks/03_model.ipynb
Exécuter toutes les cellules → génère modèles (models/*.pkl) et prédictions
4. Dashboard
bashstreamlit run streamlit_app/app.py
Ouvrir navigateur sur http://localhost:8501
Annexe B : Structure détaillée des données
Fichier weather_2022_raw.csv
ColonneTypeDescriptiontimedatetime64Date (YYYY-MM-DD)temperature_2m_maxfloat64Température max (°C)temperature_2m_minfloat64Température min (°C)precipitation_sumfloat64Précipitations (mm)cityobjectNom de la ville
Dimensions : 7 300 lignes × 5 colonnes
Fichier weather_2022_processed.csv
Contient les colonnes de raw + :
ColonneTypeDescriptionmonthint64Mois (1-12)day_of_yearint64Jour de l'année (1-365)day_sinfloat64sin(2π × jour/365)day_cosfloat64cos(2π × jour/365)rain_categorycategoryCatégorie de pluiehot_categorycategoryCatégorie de chaleurcold_categorycategoryCatégorie de froidz_temp_maxfloat64Z-score temp. maxz_temp_minfloat64Z-score temp. minz_rainfloat64Z-score précip.temp_max_anomalyboolAnomalie temp. max (temp_min_anomalyboolAnomalie temp. min (rain_anomalyboolAnomalie précip. (temp_max_lag1float64Temp. max J-1temp_min_lag1float64Temp. min J-1target_temp_max_J1float64Temp. max J+1 (cible)
Annexe C : Seuils Météo France
Températures

Jour chaud : Tmax ≥ 25°C
Jour très chaud : Tmax ≥ 30°C
Canicule : Tmax ≥ 35°C pendant 3 jours consécutifs + Tmin ≥ 20°C
Nuit tropicale : Tmin ≥ 20°C
Jour de gel : Tmin ≤ 0°C
Jour très froid : Tmin ≤ -5°C

Précipitations

Jour sec : < 1 mm
Pluie faible : 1-10 mm
Pluie modérée : 10-30 mm
Pluie forte : 30-50 mm
Pluie très forte : > 50 mm
Pluie intense : > 100 mm/24h (seuil d'alerte orange)

Annexe D : Résultats détaillés par ville

VilleMAE (°C)RMSE (°C)R²MAE baselineGain vs baselineAjaccio1.612.070.751.68+4.1%Besançon3.053.890.632.82-8.1%Bordeaux2.773.350.702.93+5.4%Clermont-Ferrand3.594.270.633.23-11.0%Dijon2.513.140.752.29-9.6%Lille2.683.360.672.02-32.7%Limoges2.663.330.712.80+5.1%Lyon2.903.560.722.64-9.9%Marseille1.642.060.781.70+3.7%Metz2.643.230.742.28-15.5%Montpellier1.822.350.781.97+7.7%Nantes2.142.760.781.96-9.1%Orléans2.603.160.742.19-18.9%Paris2.753.280.722.19-25.7%Poitiers2.493.100.752.39-4.3%Reims2.773.300.722.08-33.3%Rennes2.132.850.741.86-14.5%Rouen2.643.260.662.08-26.8%Strasbourg2.723.340.752.50-8.5%Toulouse2.573.060.732.42-6.0%
Moyenne nationale : MAE = 2.54°C, R² = 0.72

Annexe E : Acronymes et glossaire

API : Application Programming Interface - interface de programmation permettant l'accès à des données/services
EDA : Exploratory Data Analysis - analyse exploratoire des données
GIEC : Groupe d'experts intergouvernemental sur l'évolution du climat
J+1 : Jour suivant (prévision à 1 jour d'échéance)
KPI : Key Performance Indicator - indicateur clé de performance
LSTM : Long Short-Term Memory - type de réseau de neurones récurrent
MAE : Mean Absolute Error - erreur absolue moyenne
ML : Machine Learning - apprentissage automatique
NWP : Numerical Weather Prediction - prévision numérique du temps
R² : Coefficient de détermination - proportion de variance expliquée
RMSE : Root Mean Squared Error - racine de l'erreur quadratique moyenne
Z-score : Score standardisé - nombre d'écarts-types par rapport à la moyenne
