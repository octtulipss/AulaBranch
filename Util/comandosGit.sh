# Sincroniza a branch 'main' (ou 'master') com a última versão do repositório
git pull origin main

# Cria e já muda para a nova branch
git checkout -b feature/criar_sh_aula

# Adiciona todos os arquivos alterados ao 'stage' para o próximo commit
git add .

# Cria um commit com uma mensagem descritiva sobre as alterações
git commit -m "Adicionando Comandos GIT para servir como Guia Para os Alunos"

# Envia a branch 'feature/criar_sh_aula' para o GitHub
git push origin feature/criar_sh_aula



# Crie um PullRequest - No portal do GitHub

# Muda de volta para a branch principal
git checkout main

# Sincroniza a branch principal com o repositório remoto
git pull origin main

# Deleta a branch localmente
git branch -d minha-nova-funcionalidade

# Deleta a branch no repositório remoto
git push origin --delete minha-nova-funcionalidade