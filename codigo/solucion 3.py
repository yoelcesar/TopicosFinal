Python 2.7.10 (default, May 23 2015, 09:40:32) [MSC v.1500 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> ================================ RESTART ================================
>>> 
>>> blogs, palabras, datos = readfile('blogdata1.txt')
>>> palabras[:10]
[u'otro', u'otra', u'igual', u'seis', u'haber', u'importantes', u'fuera', u'esos', u'presenta', u'china']
>>> cluts = hcluster(datos, manjathan)
>>> type(cluts)
<type 'instance'>
>>> printclust(cluts,blogs)
-
  Mitos y Timos
  -
    -
      -
        -
          Cholonymous: Blog Peruano de Actualidad y Tecnolog�a
          Xataka Ciencia
        -
          Genbeta Dev
          -
            Astrof�sica    y    F�sica
            -
              Curistoria - Curiosidades y an�cdotas hist�ricas
              Experimentos caseros
      -
        Hipertextual
        -
          -
            PC World Per�
            Tecnolog�a 7
          -
            -
              Imagen astronom�a diaria - Observatorio
              -
                Naukas
                Historias de la Historia
            -
              -
                Eureka
                -
                  La mentira esta ahi fuera
                  PC World en Espa�ol
              -
                EspacioCiencia.com
                -
                  -
                    Tecnolog�a Obsoleta
                    FayerWayer
                  -
                    La Ciencia y sus Demonios
                    -
                      C�rculo Esc�ptico Argentino
                      La Ciencia para todos
    -
      El retorno de los charlatanes
      Hispasec @unaaldia
>>> 
