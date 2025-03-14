import { cn } from "@/lib/style";
import type { Chatbot } from "@/domain/schema";
import { ChatbotCard } from "@/components/chatbot/card/chatbot-card";
import { getAllAction } from "@/server-actions/chatbot/get-all";

type Props = {
	className?: string;
};

export async function ChatbotCardList({ className }: Props) {
	const state = await getAllAction();

	if (state.data.length <= 0) {
		return (
			<div className={cn("flex h-full", className)}>
				<p>データがありません</p>
			</div>
		);
	}
	return (
		<ul
			className={cn(
				"grid grid-cols-1 sm:grid-cols-2 md:grid-cols-3 justify-center items-center gap-x-5 gap-y-8",
				className,
			)}
		>
			{state.data.map((value: Chatbot, idx: number) => {
				return (
					<li
						key={idx}
						className={
							"w-full group relative flex justify-center items-center "
						}
					>
						<ChatbotCard value={value} />
					</li>
				);
			})}
		</ul>
	);
}
