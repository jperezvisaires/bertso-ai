Para escribir el borrador os recomiendo seguir varias pautas:

    1. Empezad conectando con el lector. Haced preguntas de implicación. Y exponed el tema en un párrafo. (ejemplo)
    2. Presentad brevemente quienes sois y por qué os motiva este proyecto.
    3. Enlazar lo anterior con la técnica a través de una historia. Puede ser vuestra misma historia desde que entráis en AI Saturdays, algo personal o cualquier otro ejemplo.
    4. Explicad de forma ordenada como resolvéis el problema: tipo de problema, datos, exploración, insights, modelo, etc... Lo que habéis aprendido.
    5. Exponed vuestros resultados.
    6. Volved a hacer preguntas de implicación y terminar con los pasos futuros del proyecto.
    7. Añadir link a la ppt, el código en github, la webapp o demo si tenéis..

# Can AI boost tradition?

Tradition, from latin tradere, to transmit, is act of sharing a behavior or belief from generation to generation. And as such, this heritage becomes part of our ourselves, our identity.

Innovation, in contrast, is the introduction of new ideas, of new ways or approaches that change how things were done before. This new approaches are ofthe seen as a threaten to tradition, as the adoption of new methods or behaviors tends to change way that things were done, the tradition.

However, do things need to be always like that? Can innovation be used to leverage and spread tradition among the society?

## Bertso, doinu and neurri a glimpse of the basque tradition

Among the various treasures basque culture has manged to keep alive are **bertsoak**, improvised verses with **rhyme** that are sung following a **doinu**, a melody, that has to match with certain **neurri**, or verse length.

This bertsos are typically sung in front of an audience, and, the **bertsolaris**, the basque rhyme singers, sing about different topics which are provided by the moderator, **gaijartzaile**, while they interact with the rest of bertsolaris (in a rather acid way) in pursue of the public's applause.

How does this look like? Well lets take a look of how a monder bertso saio looks like.

[youtube-ko bideoa]

# Doinus: creation and characteristics

Doinus are transmitted from generation to generation, and it is very important for bertsolaris to know them well, because they need to use the doinu suggested by the **gaijartzaile** (moderator) or the other bertsolaris to sing their bertsoz.

## How are doinus created?

## Can we improvise over the improvisation?

Bertsoz are like rap, the [batalla de gallos] happens on the fly, there is no script to follow. This means the abbility of the bertsolari to improvise becomes the cornerstone of the bertso. However, the base, the doinu, is already known by everyone, it is something fixed, rigid.

Which is a pity? Isn't it? If improvisation is part of the great art of the bertsolari... Why not providing an improvised doinu so that bertso experience becomes even more challenging and unique?

With these thoughts in mind, and with the newly adquiered Deep Learning skillset, @jperezvisaires and @klopetx had an instant match in our mind.

If there was anything that could create doinus by itself... that had to be a Generative Adversarial Network.

Could bertolarsim be revolutionized with the use of AI? 

Well... maybe not that much, but it was worth it to give it a try.


## GANS where technology and tradition (could) meet


With the insightful courses we had during the SaturdayAI lessons, we learned about the latest innovations on the field of Deep Learning, such as the different architectures, convolutional, recurrent, autoencoder... as well as the different uses such as the reinforcement learning, generative adversarial networks, reinforcement learnning.

The quesion at this point was, could the magic of generative adversarial networks used to create different things such as images, [filter etc etc] to create new doinus?

What did we need for that purpose?

# Gathering the data

Fortunetly for us (and for the basque kulture) there exists a entity, Bertsozale Elkartea, who has a webpage that includes all the known doinus, around 3000, with their meta-data included. It is in basque, but just in case you wanted to give it a look. [https://bdb.bertsozale.eus/web/doinutegia/emaitzak?bilatu=&izena=&hidden_izena=&mota=0&sortzailea=&hidden_sortzailea=&bertsolaria=&hidden_bertsolaria=&jasotzailea=&hidden_jasotzailea=&jasoa=&hidden_jasoa=&urtea=&kriterioak_gorde=1]. 
And well... you know what they say right?  It's easier to ask forgiveness than get permission... 
So... We scrapped the web.
First we downloaded the metadata of the doinus. We made a selection of the most used ones considering the number of syllables and type, and we donwloaded the 'Zortziko/Txiki' ones that had 7 syllables in the first berse followed by 6 in the second.

## Midi format

But wait a minute, donwload what exactly?
Fortunetly for us, we had the chance to download the doinus in either mp3 or midi formats.

"Midi? What's that? I know about mp3 but midi reminds me of how french people names the mid day..."

MIDI (Musical Instrument Digital Interface) is a technological standard used to transfer up to 16 information channels. It transfers messages of events that include musical notation , tone and sp)



## Feeding our little generative monster

Once the ~~lunch~~ data was ready, we just needed to feed the ~~troll~~ GAN.

We could just use the midi as input...
Well, we tryed...
...we have some problems...
... and we gave up.
You know, everyone uses Deep Learning with images, why should we do otherwise?

So instead of using midis directly, we created images with them. 
Such as this one [meter imagen]

And then 

## Finding the right data


# Okay, so how is music represented?

## Midi

## Images

# Let's do the magic

## Fitting a GAN with images

