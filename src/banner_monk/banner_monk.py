from pyfiglet import Figlet
import random

def show():
    f = Figlet(font='slant')
    print(f.renderText("it's ya boiiiiii"))

def pic():
    p = """

                                      '$&
                                      @R$k
                                    '$!!!M&
                                    @?~~~!$k
                                  '9!!~ ~~!MX
                                  @X~~   `~!$k
                                 9!!      ~~!$X
                                dR!~       `~!$>
                               XR!~         `~!$k:
                              tR!~        ::~~!!MMXXHHHH!!<:.
                             <$!xxiXX!!!~~~~~~~!!MMMMMMMMMMMMMMMXXXXx::
                        .:X@N$$$RMMX!!!!~~~~~~~~!!MMMM@@MMMMMMMMMMMMXMSMMtHHHX!
                  :xiM#"~  <$!~  `~~~!~~~~~~~~~~~!!MX!!!!!??#RR888MMMMMMMMMMMHH
           ..XH@!~`       X$!~                 '~~~!MX!!!!!!!!!!!!?MMR@@$MMMMMM
     :xiM#"~             <$!~                     '~!MM??MMX!!!!!!!!!!!!!!??#R$
XH@M!``                 :$!!                        ~!R:   `~!MM!XH!!!!!!!!!!!!
                       <$!~                         `!!M:        `~"??HHX!!!!!!
                      :$!~                           `!!R:              `!!MMMH
                     '$!~                             `~!8:                   ~
                    :$!!                               ~!!N:
                   '$!~                                 `!!N:
                  .$!!~                                  ~~!&>
                 '@!!~                                    ~!MN
                .$!!~                                     ~~!M&>
               :@$MHHHHHHHHH!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!H$N
                 PINK FLOYD:  DARK SIDE OF THE MOON  BY CHAT 95


       """

    print(p)


def lotto():
    l = random.sample(range(1,46),6)
    print(l)
   
