import { cn } from "@/lib/style";
import type { ChatbotMessage } from "@/domain/schema";
import { ChatbotMessageCard } from "@/components/chatbot/card/chatbot-message-card";
import { getAllAction } from "@/server-actions/chatbot-message/get-all";

type Props = {
	chatbotId: string;
	className?: string
};

export async function ChatbotMessageCardList({ chatbotId, className }: Props) {
	
	const state = await getAllAction(chatbotId);
	
	if (state.data.messages.length <= 0) {
		return (
			<div className={cn("flex h-full", className)}>
				<p>データがありません</p>
			</div>
		);
	}

	return (
		<ul
			className={cn("grid grid-cols-1 justify-center items-center gap-x-5 gap-y-8", className)}
		>
			{state.data.messages.map((value: ChatbotMessage, idx: number) => {
				return (
					<li
						key={idx}
						className={
							"w-full group relative flex justify-center items-center "
						}
					>
						<ChatbotMessageCard value={value} />
					</li>
				);
			})}
		</ul>
	);
}
