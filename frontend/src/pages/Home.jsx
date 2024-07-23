import { Link } from 'react-router-dom'
import { useRef } from 'react'
import {
  Button,
  Flex,
  Heading,
  Image,
  SlideFade,
  Stack,
  Text,
  useBreakpointValue,
  Box,
  Container,
} from '@chakra-ui/react'
import Card from '../components/Card';


export default function Home() {
  const saibaMaisRef = useRef(null);

  const scrollToSaibaMais = () => {
    saibaMaisRef.current.scrollIntoView({ behavior: 'smooth' });
  };

  return (
    <Box bg="#212121">
      <Stack minH={'100vh'} direction={{ base: 'column', md: 'row' }}>
        <Flex p={8} flex={1} align={'center'} justify={'center'}>
          <SlideFade in={true} offsetX="-400px" transition={{ enter: { duration: .7 } }}>
            <Stack spacing={6} w={'full'} maxW={'lg'}>
              <Heading fontSize={{ base: '3xl', md: '4xl', lg: '5xl' }}>
                <Text
                  as={'span'}
                  color="#e6e4e0"
                  position={'relative'}
                  _after={{
                    content: "''",
                    width: 'full',
                    height: useBreakpointValue({ base: '20%', md: '30%' }),
                    position: 'absolute',
                    bottom: 1,
                    left: 0,
                    bg: 'orange.400',
                    zIndex: -1,
                  }}>
                  NotiCast
                </Text>
                <br />{' '}
                <Text color={'orange.400'} as={'span'}>
                  Seu Podcast de notícias
                </Text>{' '}
              </Heading>
              <Text fontSize={{ base: 'xl',}} color="#e6e4e0">
                Descubra o poder da informação em formato de áudio com o NotiCast! Nossa inovadora plataforma utiliza inteligência artificial para transformar notícias em podcasts envolventes e dinâmicos.
              </Text>
              <Stack direction={{ base: 'column', md: 'row' }} spacing={4}>
                <Button
                  as={Link}
                  to="/podcast"
                  rounded={'full'}
                  bg={'orange.400'}
                  color={'white'}
                  _hover={{
                    bg: 'orange.500',
                  }}>
                  Gerar NotiCast
                </Button>
                <Button rounded={'full'} onClick={scrollToSaibaMais}>Saiba Mais</Button>
              </Stack>
            </Stack>
          </SlideFade>
        </Flex>
        <Flex flex={1}>
          <Image
            alt={'PodcastImage'}
            objectFit={'cover'}
            src="https://images.unsplash.com/photo-1556761175-129418cb2dfe?q=80&w=1974&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D"
          />
        </Flex>
      </Stack>
      <Box ref={saibaMaisRef} color="#e6e4e0" p={8} mt={4}>
        <Heading align="center" color="orange.400">O que é NotiCast?</Heading>
        <Text fontSize="xl" color="#e6e4e0" ml="2rem" textAlign="center" mt="1rem">O NotiCast é um site onde você coloca ao link de uma noticia e nós geramos com inteligência artificial um podcast de aproximadamente 10 minutos discorrendo sobre o tema. Nós possuimos 3 apresentadores, que você pode conhecer abaixo.</Text>
      <Container maxW={'5xl'} py={16} as={Stack} spacing={12}>
        <Stack spacing={0} align={'center'}>
          <Heading color="orange.400">Nossos Apresentadores</Heading>
          <Text color="#e6e4e0" fontSize="xl" mt="1rem">Conheça um pouco mais sobre o perfil dos nossos apresentadores</Text>
        </Stack>
        <Stack
          direction={{ base: 'column', md: 'row' }}
          spacing={{ base: 10, md: 4, lg: 10 }}>
            <Card name="Antônio" avatarLink="https://images.unsplash.com/photo-1496345875659-11f7dd282d1d?q=80&w=2070&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D" description="Fala galera! Me chamo Antônio e sou um dos hosts do NotiCast. Como cético e analítico, eu sempre procuro a lógica e os fatos. Não costumo hesitar em desafiar opiniões alheias."/>
            <Card name="Brenda" avatarLink="https://images.unsplash.com/photo-1494790108377-be9c29b29330?q=80&w=1974&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D" description="Oi gente! Meu nome é Brenda e sou uma pessoa bem otimista e empática, também sou bem confiante nas minhas opiniões e acredito que sempre há um lado positivo nas coisas."/>
            <Card name="Giovanna" avatarLink="https://images.unsplash.com/photo-1541216970279-affbfdd55aa8?q=80&w=1974&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D" description="Oi pessoal! Giovanna aqui, e sou a intermediadora do podcast kkkk! Sou ponderada e equilibrada. Sempre busco compreender os dois lados da conversa e tento ser imparcial."/>
        </Stack>
      </Container>
      </Box>  
    </Box>
  );
}
