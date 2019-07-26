import pygame.font

class Button():
  def __init__(self, ai_settings, screen, msg):
    self.screen = screen
    self.screen_rect = screen.get_rect()
    self.width, self.height = 200, 50
    self.button_color = (0, 255, 0)
    self.text_color = (255, 255, 255)
    self.font = pygame.font.SysFont(None, 48)
    self.rect = pygame.Rect(0, 0, self.width, self.height)
    self.rect.center = self.screen_rect.center
    self.prep_msg(msg)

  def prep_msg(self, msg):
# 将msg渲染成图象，并使其在按钮上居中
# 实参True表示开启反锯齿功能，这样文本的边缘更平滑
# button_color是文本的背景色，如果不指定，将使用透明背景
    self.msg_image = self.font.render(msg, True, self.text_color, self.button_color)
    self.msg_image_rect = self.msg_image.get_rect()
    self.msg_image_rect.center = self.rect.center

  def draw_button(self):
# 绘制矩形
    self.screen.fill(self.button_color, self.rect)
# 绘制文本图象
    self.screen.blit(self.msg_image, self.msg_image_rect)

