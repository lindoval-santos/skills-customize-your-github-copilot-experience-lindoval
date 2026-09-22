---
description: "Instruções para usar sempre que criar ou editar arquivos Markdown de tarefas, garantindo consistência e clareza para os alunos."
applyTo: "assignments/**/*.md"
---

# Diretrizes de Estrutura para Markdown de Tarefas

Todos os arquivos Markdown de tarefas devem seguir estas diretrizes:

## 1. Uso do Template

- Os arquivos Markdown de tarefas devem seguir a estrutura em [`templates/assignment-template.md`](../../templates/assignment-template.md).
- A tarefa deve ser criada como um arquivo `README.md`.
- Não remova ou pule seções obrigatórias do template.

## 2. Orientação das Seções

Os cabeçalhos das seções devem usar EXATAMENTE o mesmo texto do template, incluindo os ícones emoji. NÃO traduza os cabeçalhos.

- `# 📘 Atividade: [Título da Atividade]` — Substitua `[Título da Atividade]` por um nome curto e descritivo (ex: `Python Básico`, `Laços e Condicionais`, `Funções e Módulos`).
- `## 🎯 Objetivo` — Escreva 1 a 2 frases resumindo o que o aluno aprenderá ou realizará. Foque nas principais habilidades ou conceitos.
- `## 📝 Tarefas` — Para cada tarefa, use `### 🛠️ [Título da Tarefa]`:
  - Use um nome de tarefa específico e orientado à ação.
  - Na descrição, indique claramente o que o aluno deve fazer.
  - Nos requisitos, use marcadores para listar os resultados ou funcionalidades esperadas. Seja específico e mensurável.
  - Forneça exemplos de entrada e saída em blocos de código, se for útil.

Não inclua seções extras, a menos que isso tenha sido especificado explicitamente.