css = '''
<style>
.chat-message {
    padding: 1.5rem; border-radius: 0.5rem; margin-bottom: 1rem; display: flex
}
.chat-message.user {
    background-color: #2b313e
}
.chat-message.bot {
    background-color: #475063
}
.chat-message .avatar {
  width: 20%;
}
.chat-message .avatar img {
  max-width: 78px;
  max-height: 78px;
  border-radius: 50%;
  object-fit: cover;
}
.chat-message .message {
  width: 80%;
  padding: 0 1.5rem;
  color: #fff;
}
'''

bot_template = '''
<div class="chat-message bot">
    <div class="avatar">
        <img src="https://i.ibb.co/cN0nmSj/Screenshot-2023-05-28-at-02-37-21.png" style="max-height: 78px; max-width: 78px; border-radius: 50%; object-fit: cover;">
    </div>
    <div class="message">{{MSG}}</div>
</div>
'''

user_template = '''
<div class="chat-message user">
    <div class="avatar">
        <img src="data:image/png;base64,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">
    </div>    
    <div class="message">{{MSG}}</div>
</div>
'''