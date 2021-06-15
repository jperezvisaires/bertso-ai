Para escribir el borrador os recomiendo seguir varias pautas:

    1. Empezad conectando con el lector. Haced preguntas de implicación. Y exponed el tema en un párrafo. (ejemplo)
    2. Presentad brevemente quienes sois y por qué os motiva este proyecto.
    3. Enlazar lo anterior con la técnica a través de una historia. Puede ser vuestra misma historia desde que entráis en AI Saturdays, algo personal o cualquier otro ejemplo.
    4. Explicad de forma ordenada como resolvéis el problema: tipo de problema, datos, exploración, insights, modelo, etc... Lo que habéis aprendido.
    5. Exponed vuestros resultados.
    6. Volved a hacer preguntas de implicación y terminar con los pasos futuros del proyecto.
    7. Añadir link a la ppt, el código en github, la webapp o demo si tenéis..

# Can AI boost tradition?

Tradition, from latin tradere, to transmit, is the act of sharing a behavior or belief from generation to generation. And as such, this heritage becomes part of our ourselves, our identity.

Innovation, in contrast, is the introduction of new ideas, of new ways or approaches that change how things were done before. This new approaches are often seen as a threat to tradition, as the adoption of new methods or behaviors tends to change the way that things were done, the tradition.

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

Well... maybe not that much, but it was worth to give it a try.


# GANS where technology and tradition (could) meet


With the insightful courses we had during the SaturdayAI lessons, we learned about the latest innovations on the field of Deep Learning, such as the different architectures, convolutional, recurrent, autoencoder... as well as the different uses such as the reinforcement learning, generative adversarial networks, reinforcement learnning.

The quesion at this point was, could the magic of generative adversarial networks be used to create new doinus?

If so, what did we need for that purpose?

Data! Of course.

# Gathering the data

Fortunetly for us (and for the basque kulture) there exists a entity, Bertsozale Elkartea, who has a webpage that includes all the known doinus, around 3000, with their meta-data included. It is in basque, but just in case you wanted to give it a look. [https://bdb.bertsozale.eus/web/doinutegia/emaitzak?bilatu=&izena=&hidden_izena=&mota=0&sortzailea=&hidden_sortzailea=&bertsolaria=&hidden_bertsolaria=&jasotzailea=&hidden_jasotzailea=&jasoa=&hidden_jasoa=&urtea=&kriterioak_gorde=1]. 
And well... you know what they say right?  It's easier to ask forgiveness than get permission... 
So... We scrapped the web (thank you bertsozale for your work, and sorry for overloading your servers and getting your data wihout formally asking permission).
First we downloaded the metadata of the doinus. We made a selection of the most used ones considering the number of syllables and type, and we donwloaded the 'Zortziko/Txiki' ones that had 7 syllables in the first berse followed by 6 in the second which decreased the list of doinus to around 200.

## Midi format

"But wait a minute, donwload what exactly?"

Fortunetly for us, we had the chance to download the doinus in either mp3 or midi formats.

"Midi? What's that? I know about mp3 but midi reminds me of how french people names the mid day..."

MIDI (Musical Instrument Digital Interface) is a technological standard used to transfer up to 16 information channels. It transfers messages of events that include musical notation, tone and speed among other things. Basically, this files explain what notes are played, when, for how long and how loud. 

## Feeding our little generative monster

Once the ~~lunch~~ data was ready, we just needed to feed the ~~troll~~ GAN.

And our experience of using midi directly for the GAN is perfectly summarized by the following poem:

We used the midi as input
Well, at least we tryed
we faced some problems
and hence, gave up.

You know, everyone uses Deep Learning with images, why should we do otherwise?

So, instead of using midis directly, we created images with them, cause, due to the nature of the midi files, it is quite simple to visualize/represent them as images. Such as this one [meter imagen]

Once at the image domain it was easier to work with the problem, as there is much more content dealing with image and training of nets.

# GAN structure

Let's take a breath for a second. We started talking about how well GANs are supposed to work in the creation of new unheared soinus, but what are GANs exactly?

GANs were introduced in the work [https://papers.nips.cc/paper/2014/file/5ca3e9b122f61f8f06494c97b1afccf3-Paper.pdf] and are essentially two separate models that are trained together with an opposed purpose. One of the models, the generative, generates new data samples, the second model, the discriminative, tells whether the data is original or it was created by the generative model. Due to their behavior, they are typicall compared to a counterfeiter and a cop. The counterfeiter keeps improving the quality of the works while the cop gets better at detecting which ones are real or faked.

Basically, during the training process, the counterfeiter would get much better on creating new data (in this case images of new possible doinus) while the cop would imrpove on the detection of fake soinus, forcing the improvement of the counterfeiter. At some point, the generative model would be so good at creating doinus that it would become absolutely impossible for the discriminative model to discern among real or fake soinus, meaning we had a model cappable of creating good enough doinus.

Easy peasy lemon squeezy isn't it?

SPOILER: Nothing went as expected.

## Round 1: If what one has to say is not better than silence...

We started to feed our monster (well, monsters actually).
We waited until the training converged.
And we freaked out with the resulting doinus.

[imagen de midi]

Yes, this is an empty midi. Apparently our GAN was that smart that prefferred to remain silent instead saying something worse than the silence...

Why?
We didn't have many music channels nor doinus. The generator might initially learnt that, by swithing all the pixels off, it could trick the dumb discriminator. However, during the training, at some point, even the dumb discriminator was able to detect that a blank image was not a real doinu, which meant that all the effort made by the generator to produce blank images from noise were now worthless. 

Lesson: Ensure you have enough data.


## Round 2: Damn it! How cares about mixing different doinus? 

Lesson: It might happen that more data is not enough data.

## Round 3: Mixing doinus? I'm pretty sure reggae can help us on this


# Let's do the magic

