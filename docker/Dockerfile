FROM ros:noetic-ros-base
ENV DEBIAN_FRONTEND=NONINTERACTIVE

RUN ln -sf /usr/share/zoneinfo/Asia/Tokyo /etc/localtime

RUN apt update
RUN --mount=type=cache,target=/root/.cache/apt apt install -y --no-install-recommends \
    cmake \
    git \
    vim \
    tmux \
    build-essential \
    python3 \
    python3-dev \
    python3-pip \
    python3-catkin-tools \
    ros-noetic-cv-bridge \
    curl \
    wget \
    tzdata \
    tree \
    clangd \
    nodejs \
    npm \
    libgl1-mesa-dev

RUN --mount=type=cache,target=/root/.cache/pip pip3 install \
    torch \
    torchvision \
    efficientnet_pytorch \
    warmup_scheduler \
    matplotlib \
    einops \
    diffusers==0.11.1 \
    vit-pytorch \
    numpy==1.24.4 \
    wandb \
    prettytable \
    opencv-python \
    opencv-contrib-python

# neovim install
RUN cd /root/ && wget https://github.com/neovim/neovim/releases/download/stable/nvim-linux64.tar.gz
RUN cd /root/ && tar xzvf nvim-linux64.tar.gz
RUN rm /root/nvim-linux64.tar.gz
RUN mv /root/nvim-linux64 /
RUN ln -sf /nvim-linux64/bin/nvim /usr/bin/nvim

# vim/neovim setup
RUN pip3 install jedi-language-server
RUN npm install -g n
RUN n stable
RUN mkdir -p /root/.vim/undo
RUN mkdir -p /root/.vim/plugged
RUN mkdir -p /root/.config/nvim

# dotfiles
RUN git clone https://github.com/ToshikiNakamura0412/dotfiles_for_docker.git /root/dotfiles
ENV DOTFILES="/root/dotfiles"
RUN ln -sf $DOTFILES/profile.sh /etc/profile.d/profile.sh
RUN ln -sf $DOTFILES/rosconfig.sh /etc/profile.d/rosconfig.sh
RUN ln -sf $DOTFILES/vim/vimrc /root/.vimrc
RUN ln -sf $DOTFILES/vim/init.vim /root/.config/nvim/init.vim
RUN ln -sf $DOTFILES/vim/coc-settings.json /root/.config/nvim/coc-settings.json
RUN ln -sf $DOTFILES/tmux.conf /root/.tmux.conf
