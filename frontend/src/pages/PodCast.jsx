import { useState } from 'react';
import {
  Stack,
  FormControl,
  Input,
  Button,
  useColorModeValue,
  Heading,
  Text,
  Container,
  Flex,
  Box,
  Spacer,
} from '@chakra-ui/react';
import { CheckIcon } from '@chakra-ui/icons';
import { z } from 'zod';
import { zodResolver } from '@hookform/resolvers/zod';
import { useForm } from 'react-hook-form';

const urlSchema = z.object({
  url: z.string().url(),
});

export default function PodCast() {
  const [state, setState] = useState('initial');
  const [error, setError] = useState(false);
  const [downloadUrl, setDownloadUrl] = useState(null);

  const { handleSubmit, register } = useForm({
    resolver: zodResolver(urlSchema),
    mode: 'onBlur',
  });

  const onSubmit = async ({ url }) => {
    try {
      setState('submitting');
      const response = await fetch('https://noticastt-zrpffjruhq-uc.a.run.app/g1', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({ url }),
      });

      const blob = await response.blob();
      const downUrl = window.URL.createObjectURL(blob);
      setDownloadUrl(downUrl);
      setState('success');
    } catch (error) {
      setError(true);
      setState('initial');
    }
  };

  return (
    <>
      <Box align="center">
        <Heading bg="#212121" color="#e6e4e0" alignSelf={"center"}>Gere seu NotiCast</Heading>
      </Box>
      <Flex
        bg="#212121"
        minH={'calc(100vh - 60px)'}
        align={'center'}
        justify={'center'}>
        <Container
          maxW={'lg'}
          bg="gray"
          boxShadow={'xl'}
          rounded={'lg'}
          p={6}>
          {!downloadUrl ? (
            <>
              <Heading
                as={'h2'}
                color="#e6e4e0"
                fontSize={{ base: 'xl', sm: '2xl' }}
                textAlign={'center'}
                mb={5}>
                Insira o link abaixo
              </Heading>
              <Stack
                direction={{ base: 'column', md: 'row' }}
                as={'form'}
                spacing={'12px'}
                onSubmit={handleSubmit(onSubmit)}>
                <FormControl>
                  <Input
                    variant={'solid'}
                    borderWidth={1}
                    color={'gray.800'}
                    _placeholder={{
                      color: 'gray.400',
                    }}
                    borderColor={useColorModeValue('gray.300', 'gray.700')}
                    id={'url'}
                    type={'url'}
                    required
                    placeholder={'http://exemplo.com'}
                    aria-label={'URL da notícia'}
                    {...register('url')}
                    disabled={state !== 'initial'}
                  />
                </FormControl>
                <FormControl w={{ base: '100%', md: '40%' }}>
                  <Button
                    colorScheme={state === 'success' ? 'green' : 'gray'}
                    isLoading={state === 'submitting'}
                    w="100%"
                    type={state === 'success' ? 'button' : 'submit'}>
                    {state === 'success' ? <CheckIcon /> : 'Gerar'}
                  </Button>
                </FormControl>
              </Stack>
              <Text mt={2} textAlign={'center'} color={error ? 'red.500' : 'gray.500'}>
                {error && 'Ocorreu um erro! 😢 Tente novamente mais tarde.'}
              </Text>
            </>
          ) : (
            <>
            <Flex alignItems={"center"} alignSelf={"center"} justifyContent={"center"}>
              <Heading
                as={'h2'}
                color="#e6e4e0"
                fontSize={{ base: 'xl', sm: '2xl' }}
                textAlign={'center'}
                mb={5}>
                Aqui está seu NotiCast!
              </Heading>
            </Flex>
            <Flex alignItems={"center"}>
              <Box mt={4} textAlign={'center'}>
                <audio controls>
                  <source src={downloadUrl} type="audio/wav" />
                  Seu navegador não suporta o elemento de áudio.
                </audio>
              </Box>
              <Spacer />
              <Box mt={2} textAlign={'center'} alignSelf={"center"}>
                <Button bg="#e6e4e0" onClick={() => {
                  const a = document.createElement('a');
                  a.href = downloadUrl;
                  a.download = 'podcast.wav';
                  document.body.appendChild(a);
                  a.click();
                  document.body.removeChild(a);
                }}>
                  Baixar Áudio
                </Button>
              </Box>
              </Flex>
              </>
          )}
        </Container>
      </Flex>
    </>
  );
}
