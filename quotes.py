import discord






quotes = ["C'est dans le besoin qu'on reconnaît ses vrais amis.",
         "Il n'est pire aveugle que celui qui ne veut pas voir. Il n'est pire sourd que celui qui ne veut pas entendre.",
         "Les yeux ont toujours faim de voir.",
         "La patience est amère, mais son fruit est doux.",
         "A vouloir trop avoir, l'on perd tout.",
         "Quand la pauvreté entre par la porte, l'amour s'en va par la fenêtre.",
         "Donne ton amour à ta femme et donne ton secret à ta mère.",
         "Sagesse, beauté et gentillesse ne font bouillir aucun chaudron.",
         "Le mal retourne à celui qui le fait.",
         "Qui se nourrit d'attente risque de mourir de faim."]


Afro_quote_1 = [
    "La beauté n'est pas tout.",
    "Les grands projets ne se réalisent pas sans efforts.",
    "Si vous voulez aller vite, allez seul. Si vous voulez aller loin, allez ensemble.",
    "Le silence est un ami qui ne trahit jamais.",
    "Il n'y a pas de honte à ne pas savoir; la honte est de ne pas apprendre.",
    "Le véritable ami est celui qui est à vos côtés lorsque vous préférez être ailleurs.",
    "L'œil qui voit ne doit jamais s'étonner de ce qu'il voit.",
    "Si vous voulez couper un arbre en une heure, passez les premières 45 minutes à affûter la hache.",
    "Le mensonge donne des fleurs, mais pas de fruits.",
    "Un seul doigt ne peut ramasser des grains.",
    "Le fou ne se connaît pas comme tel.",
    "Le chemin est long, mais la vérité est au bout.",
    "Mieux vaut prévenir que guérir.",
    "Le travail est la meilleure des prières.",
    "On n'apprend pas à un vieux singe à faire des grimaces.",
    "La patience est le meilleur remède à tous les maux.",
    "Les parents sont les premiers éducateurs.",
    "La vie n'est pas un rêve.",
    "Les petits ruisseaux font les grandes rivières.",
    "Le destin est entre les mains de Dieu.",
    "L'homme qui ne sait pas écouter ne sait pas parler.",
    "Celui qui dit la vérité doit être prêt à l'accepter.",
    "Il n'y a pas de mal à demander de l'aide.",
    "La terre appartient à celui qui la cultive.",
    "Les paroles s'envolent, les écrits restent.",
    "La méchanceté finit toujours par être découverte.",
    "Il n'y a pas de fumée sans feu.",
    "Le chameau ne voit pas sa bosse, mais il voit celle des autres.",
    "Le savoir est une arme plus puissante que l'épée.",
    "Le mariage est comme un jardin, il faut l'entretenir.",
    "Le mensonge est un traître qui ne pardonne jamais.",
    "Mieux vaut arriver en retard que jamais.",
    "Les bonnes choses ont toujours une fin.",
    "L'homme qui ne prend pas de risques ne boit pas de champagne.",
    "L'expérience est une lanterne que l'on porte sur le dos et qui n'éclaire jamais que le chemin parcouru.",
    "La peur est le pire ennemi de l'homme.",
    "Les paroles sont comme des plumes, une fois qu'elles sont parties, on ne peut plus les reprendre.",
    "Le courage n'est pas l'absence de peur, mais la capacité de la vaincre.",
    "La richesse ne se mesure pas à l'argent que l'on possède, mais à l'amour que l'on donne.",
    "On ne peut pas empêcher les oiseaux de voler au-dessus de nos têtes, mais on peut les empêcher d'y faire leur nid.",

    ]


Afro_quote_2 = [
    "La patience est la mère de toutes les vertus.",
    "Si tu veux aller vite, marche seul. Si tu veux aller loin, marchons ensemble.",
    "Le voyage d'un millier de kilomètres commence par un pas.",
    "On ne peut pas bâtir son avenir en étant assis sur celui des autres.",
    "Le mensonge donne des fleurs, mais pas de fruits.",
    "Celui qui demande ne se trompe jamais. Celui qui ne demande pas se trompe souvent.",
    "Le savon ne doit jamais être avalé pour laver les intestins.",
    "Le silence est un ami qui ne trahit jamais.",
    "La vérité est comme l'huile, elle finit toujours par remonter à la surface.",
    "La bave du crapaud n'atteint pas la blanche colombe.",
    "Si tu veux connaître un homme, observe comment il traite ses inférieurs, pas ses égaux.",
    "Le sage parle parce qu'il a quelque chose à dire. Le fou parle parce qu'il doit dire quelque chose.",
    "L'argent peut acheter une maison, mais pas un foyer.",
    "La vie est comme un arc-en-ciel, il faut de la pluie et du soleil pour en voir les couleurs.",
    "Un seul doigt ne peut pas attraper un pou.",
    "La hâte est mauvaise conseillère.",
    "Le maître a beau enseigner, c'est l'élève qui doit apprendre.",
    "La véritable sagesse est de ne pas sembler sage.",
    "Même le lion, le roi de la jungle, a besoin de défenseurs.",
    "Celui qui se lève tôt rencontre la rosée.",
    "Le respect se gagne, il ne s'achète pas.",
    "Le succès n'est pas final, l'échec n'est pas fatal : c'est le courage de continuer qui compte.",
    "La colère est comme un cheval fougueux, si tu ne la tiens pas, elle te tiendra.",
    "Celui qui ne sait pas où il va, arrivera n'importe où.",
    "Il est plus facile de prendre un mensonge pour vérité que de convaincre celui qui croit en ce mensonge que c'est un mensonge.",
    "Le temps est comme un ruisseau, il ne revient jamais en arrière.",
    "Le mensonge court, mais la vérité le rattrape toujours.",
    "Le malheur ne vient jamais seul.",
    "Un seul arbre ne fait pas une forêt.",
    "Un seul doigt ne peut pas ramasser des cailloux.",
    "Même une petite pierre fait des vagues quand elle tombe dans l'eau.",
    "Celui qui ne fait rien ne se trompe jamais.",
    "Le mensonge est une bougie, la vérité est un soleil.",
    "Celui qui n'a jamais été malade ne se réjouit pas de la santé.",
    "La chance sourit aux audacieux.",
    "On ne peut pas être à la fois au four et au moulin.",
    "Mieux vaut tard que jamais.",
    "Qui ne risque rien n'a rien.",
    ]


# resultat = set(Afro_quote_1) & set(Afro_quote_2)
#
#
# if len(resultat) > 0:
#     print(f'il ya {len(resultat)}, element commun : {resultat}')
# else:
#     print("il n'ya pas d'element commun ")