import discord
import time
import pickle
from random import randint
from asyncio import sleep
import os

client = discord.Client()
contagem = 0
ctg_members = 0
agora = int(time.time())
idspassados = []
try:
    if os.path.getsize('data.pkl') > 0:
        with open('data.pkl', 'rb') as f:
            idspassados = pickle.load(f)
            f.close()
    else:
        with open('data.pkl', 'wb') as f:
            pickle.dump([None], f)
            f.close
except Exception as e:
    print(e)
    with open('data.pkl', 'wb') as f:
        pickle.dump([None], f)
        f.close

@client.event
async def on_ready():
    global ctg_members
    servers = list(client.servers)
    for server in client.servers:
        ctg_members += len(server.members)
    print(f"Conectado \n{len(servers)} Servers\n{ctg_members} Membros")

@client.event
async def on_member_join(member):
    global contagem
    global agora
    global idspassados
    if not member.id in idspassados:
        try:
            idspassados.append(member.id)
            with open('data.pkl', 'wb') as f:
                pickle.dump(idspassados, f)
                contagem += 1
                print(f"{client.user.name} Divulgou para {member.id}|{contagem}")
                agora = int(time.time())
                f.close()
            await sleep(randint(5,9))
            #MESSAGEM \n = ESPAÇO
            msg = await client.send_message(member,"**Venha fazer parte da nossa família da Yound Community\n:heart: ~~>https://discord.gg/7TCRA7B<~~**")
            #MESSAGEM 
            await sleep(randint(580,620))
            await client.delete_message(msg)
        except Exception as e:
            print(f"Erro: {e}")
    else:
        print(f"Esse membro já foi{member.id}")


client.run("NDg0MDQyMzU0NDAwMTY1ODkw.DmcS8w.ArotFh1Hlrt7WiSimgNmdvKr2DE",bot=False)
